concrete PropLatex of Prop = open Prelude, Formal in {


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
  PNeg = prefix 3 "\\sim" ;
  PConj = infixl 1 ;
  PImpl = infixr 0 "\\supset" ;
  PUniv v = prefix 3 (parenth ("\\forall" ++ v)) ;
  PExist v = prefix 3 (parenth ("\\exists" ++ v)) ;

  APred1 p x = \\b => appLatex (p ! b) (top x) ;
  APred2 p x y = \\b => appLatex (p ! b) (top x) (top y) ;

  IVar x = constant x ;
  IFun1 f x = constant (appLatex (top f) (top x)) ;
  IFun2 f x y = constant (appLatex (top f) (top x) (top y)) ;

  VString s = s.s ;

  CAnd = "\\&" ;
  COr = "\\vee" ;

-- supplementary

lincat
  Kind,
  [Prop],
  [Pred1], 
  [Ind], 
  [Var]
    = Str ;

lin
  AKind k x = table {True => top x ++ "\\in" ++ k ; False => top (prefix 3 "\\sim" (constant (top x ++ "\\in" ++ k)))} ;  ---- Elze: fixed negation of in

  PConjs c ps = constant (c ++ "[" ++ ps ++ "]") ;
  PUnivs vs k = prefix 4 (parenth ("\\forall" ++ vs ++ "\\in" ++ k)) ;
  PExists vs k = prefix 4 (parenth ("\\exists" ++ vs ++ "\\in" ++ k)) ;

  PNegAtom a = constant (a ! False) ;
  
  -- Elze: for existNeg
  PNegExist v = prefix 3 (parenth ("\\simexists" ++ v)) ;

  BaseProp a b = top a ++ "," ++ top b ;
  ConsProp a as = top a ++ "," ++ as ;

  BaseVar a = a ;
  ConsVar a as = a ++ "," ++ as ;

  BaseInd a b = top a ++ "," ++ top b ;
  ConsInd a as = top a ++ "," ++ as ;

  BasePred1 a b = (a ! True) ++ "," ++ (b ! True) ;
  ConsPred1 a as = (a ! True) ++ "," ++ as ;

lin
  ConjPred1 c ps = \\_ => c ++ bracket ps ; ---- neg

  APredColl f ps = \\b => appLatex (f ! b) ps ;
  APredRefl f x  = \\b => appLatex (f ! b) (top x) (top x) ;

  IFunC f ps = constant (appLatex (top f) (bracket ps)) ;

  IUniv k = constant (parenth ("\\forall" ++ k)) ;
  IExist k = constant (parenth ("\\exists" ++ k)) ;

  Everything_IUniv = constant (parenth ("\\forall")) ; --Elze: for inSituWithoutKind
  Something_IExist = constant (parenth ("\\exists")) ; --Elze: for inSituWithoutKind
  Nothing_IExist = constant (parenth ("\\simexists")) ; --Elze: for inSituWithoutKind

  ConjInd c ps = constant (c ++ bracket ps) ;

  ModKind k m = (m ! True) ++ k ; --changed by Elze

  PartPred f y = \\b => (f ! b)  ++ "to" ++ (top y) ; --changed by Elze

-- test lexicon

lin
  Vertical = slash "vertical" ;
  Horizontal = slash "horizontal" ;
  Parallel = slash "parallel" ;
  Equal = slash "equal" "notequal" ;
  Line = slash "line" ;
  Point = slash "point" ;
  Centre = slash  "centre" ;
  Intersection = slash  "intersection" ;

  Set k = appLatex ("\\set") k ;

  Even = slash "even" ;
  Odd = slash "odd" ;
  Square = slash "square" ;
  Sum = slash "sum" ;
  Product = slash "product" ;
  Nat = "N" ;

  IInt i = constant i.s ;

  Dodec = "dodec" ;
  Student = "student" ;
  Cube = "cube" ;
  Prime = "prime" ;
  Person = "person" ;
  Tet = "tetrahedron" ;
  Pet = "pet" ;
  Small = slash "small" ;
  Medium = slash "medium" ;
  Large = slash "large" ;
  Even = slash "even" ;
  Adjoins = slash "adjoins" ;
  SameCol = slash "sameCol" ;
  LeftOf = slash "leftOf" ;
  RightOf = slash "rightOf" ;
  Smaller = slash "smaller" ;
  FrontOf = slash "frontOf" ;
  Larger = slash "larger" ;
  SameRow = slash "sameRow" ;
  SameShape = slash "sameShape" ;
  SameSize = slash "sameSize" ;
  BackOf = slash "backOf" ;

oper
  appLatex = overload {
    appLatex : Str -> Str -> Str = \f,x -> f ++ curly x ;
    appLatex : Str -> Str -> Str -> Str = \f,x,y -> f ++ curly x ++ curly y ;
    } ;
  slash = overload {
    slash : Str -> Str = \f -> "\\" + f ;
    slash : Str -> TermPrec = \f -> constant ("\\" + f) ;
    slash : Str -> Bool => Str = \f -> table {True => "\\" + f ; False => top (prefix 3 "\\sim" (constant ("\\" + f)))} ; --changed by Elze
    slash : Str -> Str -> Bool => Str = \f,g -> table {True => "\\" + f ; False => "\\" + g} ; 
    } ;

  curly   : Str -> Str = \s -> "{" ++ s ++ "}" ;
  bracket : Str -> Str = \s -> "[" ++ s ++ "]" ;

}
