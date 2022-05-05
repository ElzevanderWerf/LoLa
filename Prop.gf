abstract Prop = {

flags startcat = Prop ;

cat
  Prop ;	-- proposition
  Atom ;	-- atomic formula
  Pred1 ;	-- 1-place predicate
  Pred2 ;	-- 2-place predicate
  Ind ;		-- invididual constant
  Var ;		-- individual variable
  Fun1 ;	-- unary function
  Fun2 ;	-- binary function
  Conj ;	-- conjunction

fun
  PAtom  : Atom  -> Prop ;                  -- turns an atom into a proposition
  PNeg   : Prop  -> Prop ;                  -- negation
  PConj  : Conj  -> Prop -> Prop -> Prop ;  -- conjunction
  PImpl  : Prop  -> Prop -> Prop ;          -- implication

  PUniv  : Var -> Prop -> Prop ;            -- universal quantification
  PExist : Var -> Prop -> Prop ;            -- existential quantification

  IVar   : Var -> Ind ;                     -- turns a variable into a constant

  APred1 : Pred1 -> Ind -> Atom ;           -- turns 1-place predicate and individual into atomic formula
  APred2 : Pred2 -> Ind -> Ind -> Atom ;    -- turns 2-place predicate and 2 individuals into atomic formula

  IFun1  : Fun1 -> Ind -> Ind ;             -- turns a unary function and an individual into a new individual
  IFun2  : Fun2 -> Ind -> Ind -> Ind ;      -- turns a binary function and two individuals into a new individual

  VString : String -> Var ;                 -- turns a string into a variable

  CAnd, COr : Conj ;                        -- `and' and `or' are both considered conjunctions

  PTaut     : Prop ;                        -- Elze: proposition that is always true (tautology)
  PContra   : Prop ;                        -- Elze: proposition that is always false (contradiction)


-- supplementary

cat
  Kind ;            -- kind predicate
  [Prop] {2} ;      -- list of propositions
  [Var] {1} ;       -- list of individual variables
  [Ind] {2} ;       -- list of individual constants
  [Pred1] {2} ;     -- list of predicates

fun
  PConjs  : Conj  -> [Prop] -> Prop ;       -- for flattening
  PUnivs  : [Var] -> Kind -> Prop -> Prop ; -- for moving the kind predicate out of the body
  PExists : [Var] -> Kind -> Prop -> Prop ; -- for moving the kind predicate out of the body

  PNegAtom  : Atom -> Prop ;                -- for verb negation

  PNegExist : Var -> Prop -> Prop ;         -- Elze : for existNeg

  ConjPred1 : Conj -> [Pred1] -> Pred1 ;    -- for subject-sharing aggregation

  APredColl : Pred2 -> [Ind] -> Atom ;      -- alternative for Apred2

  APredRefl : Pred2 -> Ind -> Atom ;        -- for reflexivization

  IFunC  : Fun2 -> [Ind] -> Ind ;           -- alternative for IFun2

  AKind  : Kind  -> Ind -> Atom ;           -- for expressing `x :: K' for some individual x and kind K

  IUniv  : Kind -> Ind ;                    -- for in-situ quantification
  IExist : Kind -> Ind ;                    -- for in-situ quantification

  Everything_IUniv : Ind ;                  -- Elze: for inSituWithoutKind
  Something_IExist : Ind ;                  -- Elze: for inSituWithoutKind
  Nothing_IExist : Ind ;                    -- Elze: for inSituWithoutKind

  ConjInd : Conj -> [Ind] -> Ind ;          -- for predicate-sharing aggregation

  ModKind : Kind -> Pred1 -> Kind ;         -- for modification

  PartPred : Pred2 -> Ind -> Pred1 ;        -- partial application: equal -> equal to y

-- 3. Test lexicons
-- test lexicon: geometry

fun
   Vertical, Horizontal : Pred1 ;
   Parallel, Equal : Pred2 ;
  Equal : Pred2 ; -- Elze
   Line, Point : Kind ;
   Centre : Fun1 ;
   Intersection : Fun2 ;  

   Set : Kind -> Kind ;

-- test lexicon: arithmetic

  Even, Odd    : Pred1 ;
  Nat          : Kind ;
  Square       : Fun1 ;
  Sum, Product : Fun2 ;
  IInt         : Int -> Ind ;

-- test lexicon: GGC
  Dodec, Student, Cube, Prime, Person, Tet, Pet : Kind ;
  Small, Medium, Large, Even : Pred1 ;
  Adjoins, SameCol, LeftOf, RightOf, Smaller, FrontOf, Larger, SameRow, SameShape, SameSize, BackOf : Pred2 ;

}
