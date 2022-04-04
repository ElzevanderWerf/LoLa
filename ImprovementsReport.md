# BUG FIX AND IMPROVEMENTS REPORT
**All code lines that are modified or added to the original code (at [cade-2011](https://github.com/GrammaticalFramework/gf-contrib/tree/master/cade-2011)) are commented with "Elze" and an optional explanation.**

## Bug Fixes
1. 	`PropLatex.gf`) Comment of Ranta `fix negation of in` at `lin AKind`: *1 \in N* is parsed and linearized as both *1 is a number* and *1 is not a number*. New code:
        
        AKind k x = table {True => top x ++ "\\in" ++ k ; False => top (prefix 3 "\\sim" (constant (top x ++ "\\in" ++ k)))} ;
	Now it only returns *1 is a number*.
2. 	`PropLatex.gf`) The linearization functions of `ModKind` and `PartPred` were wrong and commented out. New code:

			ModKind k m = (m ! True) ++ k ;
			PartPred f y = \\b => (f ! b)  ++ "to" ++ (top y) ;
3.	`PropLatex.gf`) *\even { 2 }* translates to *2 is even* (`PAtom (APred1  Even (IInt 2)`) AND *2 is not even* (`PNegAtom (APred1 Even (IInt 2))`). This happened because of wrong code in the `slash` operation (3rd case of the overload). New code: 

			slash : Str -> Bool => Str = \f -> table {True => "\\" + f ; False => top (prefix 3 "\\sim" (constant ("\\" + f)))} ;
		
## New Language
As an exercise, to get more acquainted with GF, I added the Dutch language to the application grammar: file `PropDut.gf`. TODO improve (er gaat volgens mij is mis met de zinsvolgorde in als-dan zinnen)

## Formula Simplification on the Logic Level
I added a new abstract syntax tree manipulation mode to the function `transfer` in `TransProp.hs`, called `MSimplify`. The function `simplify` builds a tree of possible simplification sequences, based on a large set of logic laws from the module `TransLogicLaws` in `TransLogicLaws.hs`. These laws are realized as `Prop -> Prop` functions and are based on a list of logical equivalences, taken from the book *Mathematical Methods in Linguistics* by Partee et al. (1990), and an additional few of my own (TODO right?). The formula nodes in this tree of possible simplifications are optimized (with `optimize`) and linearized into language, and the shortest of these translations is returned. 
		
## Ranta-like conversions
1. inSituWithoutKind) In-situ quantification for quantifiers without a kind predicate is added to avoid bad translations such as *for all x, x is even* (better is *everything is even*).
    - In `Prop.gf`, I added the following abstract functions:

			Everything_IUniv : Ind ;
			Something_IExist : Ind ;
    - In `PropI.gf`, I added the linearizations of these functions:

			Everything_IUniv = {s = everything_NP ; isSymbolic = False} ;
			Something_IExist = {s = something_NP ; isSymbolic = False} ;
    - In `PropLatex.gf`, I added the linearizations of these functions:

			Everything_IUniv = constant (parenth ("\\forall")) ;
			Something_IExist = constant (parenth ("\\exists")) ;
			
    - Core -> extended syntax) In `TransProp.hs`, I added two new cases to the function optimize:

			GPUniv x p | x `elem` (freeVars p) -> inSituWithoutKind GPUniv GEverything_IUniv x $ optimize p
			GPExist x p | x `elem` (freeVars p) -> inSituWithoutKind GPExist GSomething_IExist x $ optimize p
			
        And I added a new inSitu function called `inSituWithoutKind`:

			inSituWithoutKind :: (GVar -> GProp -> GProp) -> GInd -> GVar -> GProp -> GProp
			inSituWithoutKind quant qp x b = case b of
			  GPAtom (GAPred1 (GPartPred f y) z)              -> inSituWithoutKind quant qp x (GPAtom (GAPred2 f z y))
			  GPAtom (GAPred1 f y)   | y == vx                -> GPAtom (GAPred1 f qp)
			  GPAtom (GAPred1 f (GIFun1 h y))   | y == vx     -> GPAtom (GAPred1 f (GIFun1 h qp))
			  GPAtom (GAKind  f y)   | y == vx                -> GPAtom (GAKind f qp)
			  GPAtom (GAPredRefl f z)| z == vx                -> GPAtom (GAPredRefl f qp)
			  GPAtom (GAPred2 f z y) | y == vx && notFree x z -> GPAtom (GAPred2 f z qp)
			  GPAtom (GAPred2 f z y) | z == vx && notFree x y -> GPAtom (GAPred2 f qp y)
			  _ -> quant x b
			 where 
			  vx = GIVar x
			  
    - Extended -> core syntax) In `Transprop.hs`, I added two new cases to the function `iInd`:

			GEverything_IUniv -> let x = newVar 3 in GPUniv  x (f (GIVar x))
			GSomething_IExist -> let x = newVar 4 in GPExist x (f (GIVar x))