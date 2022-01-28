# BUG FIX AND IMPROVEMENTS REPORT
**All code lines that are modified or added to the original code (at [cade-2011](https://github.com/GrammaticalFramework/gf-contrib/tree/master/cade-2011)) are commented with "Elze" and an optional explanation.**

## Bug fixes
1. 	`PropLatex.gf`) Comment of Ranta `fix negation of in` at `lin AKind`: *1 \in N* is parsed and linearized as both *1 is a number* and *1 is not a number*. New code:
        
        AKind k x = table {True => top x ++ "\\in" ++ k ; False => top (prefix 3 "\\sim" (constant (top x ++ "\\in" ++ k)))} ;
	Now it only returns *1 is a number*.
2. 	`PropLatex.gf`) The linearization functions of `ModKind` and `PartPred` were wrong and commented out. New code:

			ModKind k m = (m ! True) ++ k ;
			PartPred f y = \\b => (f ! b)  ++ "to" ++ (top y) ;
3.	`PropLatex.gf`) *\even { 2 }* translates to *2 is even* (`PAtom (APred1  Even (IInt 2)`) AND *2 is not even* (`PNegAtom (APred1 Even (IInt 2))`). This happened because of wrong code in the `slash` operation (3rd case of the overload). New code: 

			slash : Str -> Bool => Str = \f -> table {True => "\\" + f ; False => top (prefix 3 "\\sim" (constant ("\\" + f)))} ;
		
## New language
I added the Dutch language to the application grammar: file `PropDut.gf`.
		
		
## IMPROVING TRANSLATIONS
1. In-situ quantification for quantifiers without a kind predicate is not in the list of Haskell conversions, but should be added to avoid bad translations such as *for all x, x is even* (better is *everything is even*). This is how I added in-situ quantification for quantifiers without a kind predicate:
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
		
		  
	
	
## TODOs left:
- Extend lexicon? More-place predicates? Higher-order functions? Iff? Equality function?
- Formulas such as *P \& Q \vee R* are accepted by the system, but actually are not well-formed (they are ambiguous because they miss parentheses). Solve this.
- *( \forall x \in N ) ( \even { x } \supset \sim \odd { x } )* translates to *for all numbers x , if x is even , then x is not odd*. This happens because x occurs twice in the quantified proposition. Solution: use anaphora to make it exactly one occurrence: *for all numbers x, if x is even, then it is not odd*. Now in-situ quantification can be done.