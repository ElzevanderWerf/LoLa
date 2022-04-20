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
4.  `TransProp.hs`) The function `iAtom` did not have an exhaustive list of patterns. I added the following line for the last case:

        _ -> GPAtom a
		
## New Language
As an exercise, to get more acquainted with GF, I added the Dutch language to the application grammar: file `PropDut.gf`.
		
## Ranta-like conversions
Code lines for added conversions are commented with *Elze: for inSituWithoutKind*, *Elze: for reflNegPred*, et cetera.
1. inSituWithoutKind) In-situ quantification for quantifiers without a kind predicate is added to avoid bad translations such as *for all x, x is even* (better is *everything is even*). 
2. reflNegPred) Sometimes 2-place predicates that have the same two individuals as its arguments are not converted into a reflexive in the function `optimize`. This happenes due to two reasons: (1) negated atoms are not further optimized, and (2) the predicates are parsed as APredColls instead of APred2s. I have fixed both problems.
3. existNeg) In a case that an existential quantifier is negated, the negation is moved inward, because the earlier translation "it is not the case that there exists an element x such that" is quite ugly. New translation: "there is no element x such that".
4. aggregPred2) In the original version of the code, no aggregation was done for 2-place predicates. I added this option, so that sentences like "a is parallel to b and a is parallel to c" can be aggregated to "a is parallel to b and c". I have done this for what I call predicate-sharing atoms that share either their subject or object argument.
        TODO does not yet work for subformulas of formulas :-\
        
## Formula Simplification on the Logic Level
I added a new abstract syntax tree manipulation mode to the function `transfer` in `TransProp.hs`, called `MSimplify`. The function `simplify` builds a tree of possible simplification sequences up to a maximum depth, based on a large set of logic laws from the module `TransLogicLaws` in `TransLogicLaws.hs`. These laws are realized as `Prop -> Prop` functions and are based on a list of logical equivalences, taken from the book *Mathematical Methods in Linguistics* by Partee et al. (1990), and two additional ones for vacuous quantification. The formula nodes in this tree of possible simplifications are optimized (with `optimize`) and linearized into language, and the shortest of these translations is returned. 
