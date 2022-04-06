--# -path=.:present

concrete PropDut of Prop = PropI with 
  (Syntax = SyntaxDut), 
  (Symbolic = SymbolicDut), 
  (Symbol = SymbolDut),
  (Sentence = SentenceDut)
   ** open (P = ParadigmsDut), IrregDut, Prelude, ResDut in {

flags coding = utf8 ;

-- no exceptions?


-- instance of interface

oper
  case_N = P.mkN "geval" P.het;
  such_A = P.invarA "zo" ;
  then_Adv = P.mkAdv "dan" ;
  element_N = P.mkN "element" ;
  set_N2 = P.mkN2 (P.mkN "set") ;
  hold_V = IrregDut.gelden_V ;

  singular = Sg ; -- ! cannot find paradigm singular for dutch

-- test lexicon

lin
  Vertical = mkAP (P.mkA "verticaal" "verticale") ;
  Horizontal = mkAP (P.mkA "horizontaal" "horizontale") ;
  Parallel = P.mkA2 (P.mkA "evenwijdig") (P.mkPrep "aan") ;
  Equal = P.mkA2 (P.mkA "gelijk") (P.mkPrep "aan");
  Line = mkCN (P.mkN "lijn") ;
  Point = mkCN (P.mkN "punt") ;
  Centre = mkFun1 "centre" (P.mkN "middelpunt" P.het) P.van_Prep ;
  Intersection = mkFun2 "intersection" (P.mkN "snijpunt" P.het) P.van_Prep ; --same here

  Set k = mkCN set_N2 (mkNP a_Art plNum k) ; --? keep like this?

  Even = mkAP (P.invarA "even") ; --or mkA? 
  Odd = mkAP (P.invarA "oneven") ;
  Square = mkFun1 "square" (P.mkN "kwadraat" P.het) P.van_Prep ;
  Sum = mkFun2 "sum" (P.mkN "som") P.van_Prep ;
  Product = mkFun2 "product" (P.mkN "product" P.het) P.van_Prep ;
  Nat = mkCN (P.mkN "getal" P.het) ;

oper
  mkFun1, mkFun2 : Str -> N -> Prep -> {s : Symb ; v : N2} = \s,n,p -> 
    {s = mkSymb ("\\" + s) ; v = P.mkN2 n p} ;

}
