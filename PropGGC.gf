concrete PropGGC of Prop = open Prelude, Formal in {

lincat
  Prop = TermPrec ;
  Atom = Bool => Str ;
  Pred1 = Bool => Str ;
  Pred2 = Bool => Str ;
  Var,
  Conj
    = Str ;
  Ind = TermPrec ;
  Fun1 = TermPrec ;
  Fun2 = TermPrec ;

lin
  PAtom a = constant (a ! True) ;
  PNeg = prefix 3 "~" ;
  PConj = infixl 1 ;
  PImpl = infixr 0 "$" ;
  PUniv v = prefix 3 ("@" ++ v) ;
  PExist v = prefix 3 ("/" ++ v) ;

  APred1 p x = \\b => appGGC (p ! b) (top x) ;
  APred2 p x y = \\b => appGGC (p ! b) (top x) (top y) ;

  IVar x = constant x ;
  IFun1 f x = constant (appGGC (top f) (top x)) ;
  IFun2 f x y = constant (appGGC (top f) (top x) (top y)) ;

  VString s = s.s ;

  CAnd = "&" ;
  COr = "|" ;

-- supplementary

lincat
  Kind = Str ;
  [Prop],
  [Pred1], 
  [Ind], 
  [Var]
    = Str ;

lin
  AKind k x = table {True => appGGC k (top x) ; False => "~" ++ (appGGC k (top x)) } ;

  --PConjs c ps = constant (c ++ "[" ++ ps ++ "]") ; --not part of ggc?
  --PUnivs vs k = prefix 4 (parenth ("\\forall" ++ vs ++ "\\in" ++ k)) ; --not part of ggc?
  --PExists vs k = prefix 4 (parenth ("\\exists" ++ vs ++ "\\in" ++ k)) ; --not part of ggc?

  --PNegAtom a = constant (a ! False) ; --not part of ggc?

  --BaseProp a b = top a ++ "," ++ top b ; --not part of ggc?
  --ConsProp a as = top a ++ "," ++ as ; --not part of ggc?

  --BaseVar a = a ; --not part of ggc?
  --ConsVar a as = a ++ "," ++ as ; --not part of ggc?

  --BaseInd a b = top a ++ "," ++ top b ; --not part of ggc?
  --ConsInd a as = top a ++ "," ++ as ; --not part of ggc?

  --BasePred1 a b = (a ! True) ++ "," ++ (b ! True) ; --not part of ggc?
  --ConsPred1 a as = (a ! True) ++ "," ++ as ; --not part of ggc?

--lin
  --ConjPred1 c ps = \\_ => c ++ bracket ps ; ---- neg --not part of ggc?

  --APredColl f ps = \\b => appLatex (f ! b) ps ; --not part of ggc?
  --APredRefl f x  = \\b => appLatex (f ! b) (top x) (top x) ; --not part of ggc?

  --IFunC f ps = constant (appLatex (top f) (bracket ps)) ; --not part of ggc?

  --IUniv k = constant (parenth ("\\forall" ++ k)) ; --not part of ggc?
  --IExist k = constant (parenth ("\\exists" ++ k)) ; --not part of ggc?

  --ConjInd c ps = constant (c ++ bracket ps) ; --not part of ggc?

  --ModKind k m = (m ! True) ++ k ; -- Elze --not part of ggc?
  --PartPred f y = \\b => (f ! b)  ++ "to" ++ (top y) ;  -- Elze --not part of ggc?

-- test lexicon

lin
--  Vertical = slash "vertical" ;
--  Horizontal = slash "horizontal" ;
--  Parallel = slash "parallel" ;
--  Equal = slash "equal" "notequal" ;
--  Line = slash "line" ;
--  Point = slash "point" ;
--  Centre = slash  "centre" ;
--  Intersection = slash  "intersection" ;

--  Set k = appLatex ("\\set") k ;

--  Even = slash "even" ;
--  Odd = slash "odd" ;
--  Square = slash "square" ;
--  Sum = slash "sum" ;
--  Product = slash "product" ;
--  Nat = "N" ;

  IInt i = constant i.s ;

  Dodec = "Dodec" ;
  Student = "Student" ;
  Cube = "Cube" ;
  Prime = "Prime" ;
  Person = "Person" ;
  Tet = "Tet" ;
  Pet = "Pet" ;
  Small = slashGGC "Small" ;
  Medium = slashGGC "Medium" ;
  Large = slashGGC "Large" ;
  Even = slashGGC "Even" ;
  Adjoins = slashGGC "Adjoins" ;
  SameCol = slashGGC "SameCol" ;
  LeftOf = slashGGC "LeftOf" ;
  RightOf = slashGGC "RightOf" ;
  Smaller = slashGGC "Smaller" ;
  FrontOf = slashGGC "FrontOf" ;
  Larger = slashGGC "Larger" ;
  SameRow = slashGGC "SameRow" ;
  SameShape = slashGGC "SameShape" ;
  SameSize = slashGGC "SameSize" ;
  BackOf = slashGGC "BackOf" ;

oper
  appGGC = overload {
    appGGC : Str -> Str -> Str = \f,x -> f ++ curly x ;
    appGGC : Str -> Str -> Str -> Str = \f,x,y -> f ++ curly (x ++ "," ++ y);
    } ;
  slash = overload {
    slash : Str -> Str = \f -> "\\" + f ;
    slash : Str -> TermPrec = \f -> constant ("\\" + f) ;
    slash : Str -> Bool => Str = \f -> table {True => "\\" + f ; False => top (prefix 3 "\\sim" (constant ("\\" + f)))} ; -- Elze
    slash : Str -> Str -> Bool => Str = \f,g -> table {True => "\\" + f ; False => "\\" + g} ; 
    } ;
  slashGGC : Str -> Bool => Str = \f -> table {True => f ; False => top (prefix 3 "~" (constant (f)))} ;
  

  curly : Str -> Str = \s -> "(" ++ s ++ ")" ;
  bracket : Str -> Str = \s -> "[" ++ s ++ "]" ;

}
