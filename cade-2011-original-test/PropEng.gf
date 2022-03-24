--# -path=.:present

concrete PropEng of Prop = PropI - [PNeg, PNegAtom] with 
  (Syntax = SyntaxEng), 
  (Symbolic = SymbolicEng),
  (Sentence = SentenceEng)
   ** open (P = ParadigmsEng), ExtraEng, Prelude in {

-- exceptions

lin
  PNeg p = { 
    s = mkS ExtraEng.UncNeg (mkCl 
          (mkVP (mkNP the_Quant (mkCN case_N (mkAdv that_Subj p.s))))) ; 
    c = False ---- ?
    } ;
  PNegAtom a = {
    s = mkS ExtraEng.UncNeg a ;
    c = False
    } ;

-- instance of interface

oper
  case_N = P.mkN "case" ;
  such_A = P.mkA "such" ;
  then_Adv = P.mkAdv "then" ;
  element_N = P.mkN "element" ;
  set_N2 = P.mkN2 (P.mkN "set") ;
  hold_V = P.mkV "hold" "held" "held" ;

  singular = P.singular ; ---

-- test lexicon

lin
--  Vertical = mkAP (P.mkA "vertical") ;
--  Horizontal = mkAP (P.mkA "horizontal") ;
--  Parallel = P.mkA2 (P.mkA "parallel") to_Prep ;
--  Equal = P.mkA2 (P.mkA "equal") to_Prep ;
--  Line = mkCN (P.mkN "line") ;
--  Point = mkCN (P.mkN "point") ;
--  Centre = mkFun1 "centre" ;
--  Intersection = mkFun2 "intersection" ;

--  Set k = mkCN set_N2 (mkNP a_Art plNum k) ; 

--  Even = mkAP (P.mkA "even") ;
--  Odd = mkAP (P.mkA "odd") ;
--  Square = mkFun1 "square" ;
--  Sum = mkFun2 "sum" ;
--  Product = mkFun2 "product" ;
--  Nat = mkCN (P.mkN "number") ;

  Dodec = mkCN (P.mkN "dodecahedron") ;
  Student = mkCN (P.mkN "student") ;
  Cube = mkCN (P.mkN "cube") ;
  Prime = mkCN (P.mkN "prime") ;
  Person = mkCN (P.mkN "person") ;
  Tet = mkCN (P.mkN "tetrahedron") ;
  Pet = mkCN (P.mkN "pet") ;
  Small = mkAP (P.mkA "small") ;
  Medium = mkAP (P.mkA "medium") ;
  Large = mkAP (P.mkA "large") ;
  Even = mkAP (P.mkA "even") ;
  Adjoins = P.mkA2 (P.mkA "adjacent") to_Prep ;
  SameCol = P.mkA2 (P.mkA "in the same column") (P.mkPrep "as") ;
  LeftOf = P.mkA2 (P.mkA "to the left") (P.mkPrep "of") ;
  RightOf = P.mkA2 (P.mkA "to the right") (P.mkPrep "of") ;
  Smaller = P.mkA2 (P.mkA "smaller") (P.mkPrep "than") ;
  FrontOf = P.mkA2 (P.mkA "in front") (P.mkPrep "of") ;
  Larger = P.mkA2 (P.mkA "larger") (P.mkPrep "than") ;
  SameRow = P.mkA2 (P.mkA "in the same row") (P.mkPrep "as") ;
  SameShape = P.mkA2 (P.mkA "of the same shape") (P.mkPrep "as") ;
  SameSize = P.mkA2 (P.mkA "of the same size") (P.mkPrep "as") ;
  BackOf = P.mkA2 (P.mkA "in back") (P.mkPrep "of") ;
  

oper
  mkFun1, mkFun2 : Str -> {s : Symb ; v : N2} = \s -> 
    {s = mkSymb  ("\\" + s) ; v = P.mkN2 (P.mkN s)} ;

}
