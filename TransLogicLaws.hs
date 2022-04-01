{-# LANGUAGE PackageImports #-}
{-# LANGUAGE GADTs #-}
{-# OPTIONS_GHC -fglasgow-exts #-}

module TransLogicLaws where

import qualified "gf" PGF (Tree, showExpr, showCId, exprFunctions)
import Prop   -- generated from GF
import Data.List (isInfixOf)
import TransPropFunctions

logicLaws = [idempotence1, idempotence2, associativity1ltr, associativity1rtl, 
  associativity2ltr, associativity2rtl, commutativity1, commutativity2, 
  distributivity1ltr, distributivity1rtl, distributivity2ltr, distributivity2rtl, 
  identity1, identity2, identity3, identity4, complement1, complement2, 
  complement3, deMorgan1ltr, deMorgan1rtl, deMorgan2ltr, deMorgan2rtl, 
  conditional1ltr, conditional1rtl, conditional2ltr, conditional2rtl, 
  quantneg1ltr, quantneg1rtl, quantneg2ltr, quantneg2rtl, quantneg3ltr,
  quantneg3rtl, quantneg4ltr, quantneg4rtl, quantdist1ltr, quantdist1rtl,
  quantdist2ltr, quantdist2rtl, quantdist3, quantdist4, quantind1, quantind2,
  quantind3, quantmov1ltr, quantmov1rtl, quantmov2ltr, quantmov2rtl,
  quantmov3ltr, quantmov3rtl, quantmov4ltr, quantmov4rtl, vacquant1, vacquant2]
  
identityLaws = [identity1, identity2, identity3, identity4]
  
-- Two-way logical equivalence functions are named rtl and ltr 
-- (rtl = right-to-left, ltr = left-to-right). Some equivalence functions only
-- have a ltr function, because the translation is shortened only in that direction


-- PROPOSITIONAL LOGIC EQUIVALENCES
-- Idempotence 1 (only ltr): p \vee p <-> p
idempotence1 :: GProp -> GProp
idempotence1 = ip1
ip1 :: forall c. Tree c -> Tree c
ip1 p = case p of
  GPConj GCOr p1 p2 | p1 == p2 -> p1
  _ -> composOp ip1 p
  
-- Idempotence 2 (only ltr): p \& p <-> p
idempotence2 :: GProp -> GProp
idempotence2 = ip2
ip2 :: forall c. Tree c -> Tree c
ip2 p = case p of
  GPConj GCAnd p1 p2 | p1 == p2 -> p1
  _ -> composOp ip1 p
  
-- Associativity 1: (p \vee q) \vee r <-> p \vee (q \vee r)
associativity1ltr :: GProp -> GProp
associativity1ltr = ass1ltr
ass1ltr :: forall c. Tree c -> Tree c
ass1ltr p = case p of
  GPConj GCOr (GPConj GCOr p1 p2) p3 -> GPConj GCOr p1 (GPConj GCOr p2 p3)
  _ -> composOp ass1ltr p
  
associativity1rtl :: GProp -> GProp
associativity1rtl = ass1rtl
ass1rtl :: forall c. Tree c -> Tree c
ass1rtl p = case p of
  GPConj GCOr p1 (GPConj GCOr p2 p3) -> GPConj GCOr (GPConj GCOr p1 p2) p3
  _ -> composOp ass1rtl p
  
-- Associativity 2: (p \& q) \& r <-> p \& (q \& r)
associativity2ltr :: GProp -> GProp
associativity2ltr = ass2ltr
ass2ltr :: forall c. Tree c -> Tree c
ass2ltr p = case p of
  GPConj GCAnd (GPConj GCAnd p1 p2) p3 -> GPConj GCAnd p1 (GPConj GCAnd p2 p3)
  _ -> composOp ass2ltr p
  
associativity2rtl :: GProp -> GProp
associativity2rtl = ass2rtl
ass2rtl :: forall c. Tree c -> Tree c
ass2rtl p = case p of
  GPConj GCAnd p1 (GPConj GCAnd p2 p3) -> GPConj GCAnd (GPConj GCAnd p1 p2) p3
  _ -> composOp ass2rtl p
  
-- Commutativity 1 (ltr and rtl are the same): p \vee q <-> q \vee p
commutativity1 :: GProp -> GProp
commutativity1 = comm1
comm1 :: forall c. Tree c -> Tree c
comm1 p = case p of
  GPConj GCOr p1 p2 -> GPConj GCOr p2 p1
  _ -> composOp comm1 p
  
-- Commutativity 2 (ltr and rtl are the same): p \& q <-> q \& p
commutativity2 :: GProp -> GProp
commutativity2 = comm2
comm2 :: forall c. Tree c -> Tree c
comm2 p = case p of
  GPConj GCAnd p1 p2 -> GPConj GCAnd p2 p1
  _ -> composOp comm2 p
  
-- Distributivity 1: p \vee (q \& r) <-> (p \vee q) \& (p \vee r)
distributivity1ltr :: GProp -> GProp
distributivity1ltr = dist1ltr
dist1ltr :: forall c. Tree c -> Tree c
dist1ltr p = case p of
  GPConj GCOr p1 (GPConj GCAnd p2 p3) -> GPConj GCAnd (GPConj GCOr p1 p2) (GPConj GCOr p1 p3)
  _ -> composOp dist1ltr p
  
distributivity1rtl :: GProp -> GProp
distributivity1rtl = dist1rtl
dist1rtl :: forall c. Tree c -> Tree c
dist1rtl p = case p of
  GPConj GCAnd (GPConj GCOr p1 p2) (GPConj GCOr p3 p4) | p1 == p3 -> GPConj GCOr p1 (GPConj GCAnd p2 p4)
  _ -> composOp dist1rtl p
  
-- Distributivity 2: p \& (q \vee r) <-> (p \& q) \vee (p \& r)
distributivity2ltr :: GProp -> GProp
distributivity2ltr = dist2ltr
dist2ltr :: forall c. Tree c -> Tree c
dist2ltr p = case p of
  GPConj GCAnd p1 (GPConj GCOr p2 p3) -> GPConj GCOr (GPConj GCAnd p1 p2) (GPConj GCAnd p1 p3)
  _ -> composOp dist2ltr p
  
distributivity2rtl :: GProp -> GProp
distributivity2rtl = dist2rtl
dist2rtl :: forall c. Tree c -> Tree c
dist2rtl p = case p of
  GPConj GCOr (GPConj GCAnd p1 p2) (GPConj GCAnd p3 p4) | p1 == p3 -> GPConj GCAnd p1 (GPConj GCOr p2 p4)
  _ -> composOp dist2rtl p
  
-- Identity 1 (only ltr): p \vee F <-> p
identity1 :: GProp -> GProp
identity1 = id1
id1 :: forall c. Tree c -> Tree c
id1 p = case p of
  GPConj GCOr p1 GPContra -> p1
  _ -> composOp id1 p
  
-- Identity 2 (only ltr): p \vee T <-> T
identity2 :: GProp -> GProp
identity2 = id2
id2 :: forall c. Tree c -> Tree c
id2 p = case p of
  GPConj GCOr p1 GPTaut -> GPTaut
  _ -> composOp id2 p
  
-- Identity 3 (only ltr): p \& F <-> F
identity3 :: GProp -> GProp
identity3 = id3
id3 :: forall c. Tree c -> Tree c
id3 p = case p of
  GPConj GCAnd p1 GPContra -> GPContra
  _ -> composOp id3 p
  
-- Identity 4 (only ltr): p \& T <-> p
identity4 :: GProp -> GProp
identity4 = id4
id4 :: forall c. Tree c -> Tree c
id4 p = case p of
  GPConj GCAnd p1 GPTaut -> p1
  _ -> composOp id4 p
  
-- Complement 1 (only ltr): p \vee \sim p <-> T
complement1 :: GProp -> GProp
complement1 = comp1
comp1 :: forall c. Tree c -> Tree c
comp1 p = case p of
  GPConj GCOr p1 (GPNeg p2) | p1 == p2 -> GPTaut
  GPConj GCOr (GPAtom a1) (GPNegAtom a2) | a1 == a2 -> GPTaut
  _ -> composOp comp2 p
  
-- Complement 2 (double negation) (only ltr): \sim \sim p <-> p 
complement2 :: GProp -> GProp
complement2 = comp2
comp2 :: forall c. Tree c -> Tree c
comp2 p = case p of
  GPNeg (GPNeg p1) -> p1
  GPNeg (GPNegAtom a1) -> GPAtom a1
  _ -> composOp comp2 p
  
-- Complement 3 (only ltr): p \& \sim p <-> F
complement3 :: GProp -> GProp
complement3 = comp1
comp3 :: forall c. Tree c -> Tree c
comp3 p = case p of
  GPConj GCAnd p1 (GPNeg p2) | p1 == p2 -> GPContra
  GPConj GCAnd (GPAtom a1) (GPNegAtom a2) | a1 == a2 -> GPContra
  _ -> composOp comp3 p
  
-- De Morgan 1: \sim (p \vee q) <-> \sim p \& \sim q
deMorgan1ltr :: GProp -> GProp
deMorgan1ltr = dm1ltr
dm1ltr :: forall c. Tree c -> Tree c
dm1ltr p = case p of
  GPNeg (GPConj GCOr p1 p2) -> GPConj GCAnd (GPNeg p1) (GPNeg p2)
  _ -> composOp dm1ltr p
  
deMorgan1rtl :: GProp -> GProp
deMorgan1rtl = dm1rtl
dm1rtl :: forall c. Tree c -> Tree c
dm1rtl p = case p of
  GPConj GCAnd (GPNeg p1) (GPNeg p2) -> GPNeg (GPConj GCOr p1 p2)
  GPConj GCAnd (GPNeg p1) (GPNegAtom a1) -> GPNeg (GPConj GCOr p1 (GPAtom a1))
  GPConj GCAnd (GPNegAtom a1) (GPNeg p1) -> GPNeg (GPConj GCOr (GPAtom a1) p1)
  GPConj GCAnd (GPNegAtom a1) (GPNegAtom a2) -> GPNeg (GPConj GCOr (GPAtom a1) (GPAtom a2))
  _ -> composOp dm1rtl p
  
-- De Morgan 2: \sim (p \& q) <-> \sim p \vee \sim q
deMorgan2ltr :: GProp -> GProp
deMorgan2ltr = dm2ltr
dm2ltr :: forall c. Tree c -> Tree c
dm2ltr p = case p of
  GPNeg (GPConj GCAnd p1 p2) -> GPConj GCOr (GPNeg p1) (GPNeg p2)
  _ -> composOp dm2ltr p
  
deMorgan2rtl :: GProp -> GProp
deMorgan2rtl = dm2rtl
dm2rtl :: forall c. Tree c -> Tree c
dm2rtl p = case p of
  GPConj GCOr (GPNeg p1) (GPNeg p2) -> GPNeg (GPConj GCAnd p1 p2)
  GPConj GCOr (GPNeg p1) (GPNegAtom a1) -> GPNeg (GPConj GCAnd p1 (GPAtom a1))
  GPConj GCOr (GPNegAtom a1) (GPNeg p1) -> GPNeg (GPConj GCAnd (GPAtom a1) p1)
  GPConj GCOr (GPNegAtom a1) (GPNegAtom a2) -> GPNeg (GPConj GCAnd (GPAtom a1) (GPAtom a2))
  _ -> composOp dm2rtl p
  
-- Conditional 1: p \supset q <-> \sim p \vee q
conditional1ltr :: GProp -> GProp
conditional1ltr = cond1ltr
cond1ltr :: forall c. Tree c -> Tree c
cond1ltr p = case p of
  GPImpl p1 p2 -> GPConj GCOr (GPNeg p1) (p2)
  _ -> composOp cond1ltr p
  
conditional1rtl :: GProp -> GProp
conditional1rtl = cond1rtl
cond1rtl :: forall c. Tree c -> Tree c
cond1rtl p = case p of
  GPConj GCOr (GPNeg p1) (p2) -> GPImpl p1 p2
  GPConj GCOr (GPNegAtom a1) (p1) -> GPImpl (GPAtom a1) p1
  _ -> composOp cond1rtl p
  
-- Conditional 2 (contraposition): p \supset q <-> \sim q \supset \sim p
conditional2ltr :: GProp -> GProp
conditional2ltr = cond2ltr
cond2ltr :: forall c. Tree c -> Tree c
cond2ltr p = case p of
  GPImpl p1 p2 -> GPImpl (GPNeg p2) (GPNeg p1)
  _ -> composOp cond2ltr p
  
conditional2rtl :: GProp -> GProp
conditional2rtl = cond2rtl
cond2rtl :: forall c. Tree c -> Tree c
cond2rtl p = case p of
  GPImpl (GPNeg p1) (GPNeg p2) -> GPImpl p2 p1
  GPImpl (GPNeg p1) (GPNegAtom a1) -> GPImpl (GPAtom a1) p1
  _ -> composOp cond2rtl p
  
-- FIRST-ORDER LOGIC EQUIVALENCES AND CONSEQUENCES
-- Quantifier negation 1: \sim (\forall x) \phi(x) <-> (\exists x) \sim phi(x)
quantneg1ltr :: GProp -> GProp
quantneg1ltr = qn1ltr
qn1ltr :: forall c. Tree c -> Tree c
qn1ltr p = case p of
  GPNeg (GPUniv v1 p1) | v1 `elem` (freeVars p1) -> GPExist v1 (GPNeg p1)
  _ -> composOp qn1ltr p
  
quantneg1rtl :: GProp -> GProp
quantneg1rtl = qn1rtl
qn1rtl :: forall c. Tree c -> Tree c
qn1rtl p = case p of
  GPExist v1 (GPNeg p1) | v1 `elem` (freeVars p1) -> GPNeg (GPUniv v1 p1)
  GPExist v1 (GPNegAtom a1) | v1 `elem` (freeVars (GPAtom a1)) -> GPNeg (GPUniv v1 (GPAtom a1))
  _ -> composOp qn1rtl p
  
-- Quantifier negation 2: (\forall x) \phi(x) <-> \sim (\exists x) \sim phi(x)
quantneg2ltr :: GProp -> GProp
quantneg2ltr = qn2ltr
qn2ltr :: forall c. Tree c -> Tree c
qn2ltr p = case p of
  GPUniv v1 p1 | v1 `elem` (freeVars p1) -> GPNeg (GPExist v1 (GPNeg p1))
  _ -> composOp qn2ltr p
  
quantneg2rtl :: GProp -> GProp
quantneg2rtl = qn2rtl
qn2rtl :: forall c. Tree c -> Tree c
qn2rtl p = case p of
  GPNeg (GPExist v1 (GPNeg p1)) | v1 `elem` (freeVars p1) -> GPUniv v1 p1
  GPNeg (GPExist v1 (GPNegAtom a1)) | v1 `elem` (freeVars (GPAtom a1)) -> GPUniv v1 (GPAtom a1)
  _ -> composOp qn2rtl p
  
-- Quantifier negation 3: \sim (\forall x) \sim \phi(x) <-> (\exists x) phi(x)
quantneg3ltr :: GProp -> GProp
quantneg3ltr = qn3ltr
qn3ltr :: forall c. Tree c -> Tree c
qn3ltr p = case p of
  GPNeg (GPUniv v1 (GPNeg p1)) | v1 `elem` (freeVars p1) -> GPExist v1 p1
  GPNeg (GPUniv v1 (GPNegAtom a1)) | v1 `elem` (freeVars (GPAtom a1)) -> GPExist v1 (GPAtom a1)
  _ -> composOp qn3ltr p
  
quantneg3rtl :: GProp -> GProp
quantneg3rtl = qn3rtl
qn3rtl :: forall c. Tree c -> Tree c
qn3rtl p = case p of
  GPExist v1 p1 | v1 `elem` (freeVars p1) -> GPNeg (GPUniv v1 (GPNeg p1)) 
  _ -> composOp qn3rtl p
  
-- Quantifier negation 4: \sim (\forall x) \phi(x) <-> (\exists x) \sim phi(x)
quantneg4ltr :: GProp -> GProp
quantneg4ltr = qn4ltr
qn4ltr :: forall c. Tree c -> Tree c
qn4ltr p = case p of
  GPUniv v1 (GPNeg p1) | v1 `elem` (freeVars p1) -> GPNeg (GPExist v1 p1)
  GPUniv v1 (GPNegAtom a1) | v1 `elem` (freeVars (GPAtom a1)) -> GPNeg (GPExist v1 (GPAtom a1))
  _ -> composOp qn4ltr p
  
quantneg4rtl :: GProp -> GProp
quantneg4rtl = qn4rtl
qn4rtl :: forall c. Tree c -> Tree c
qn4rtl p = case p of
  GPNeg (GPExist v1 p1) | v1 `elem` (freeVars p1) -> GPUniv v1 (GPNeg p1)
  _ -> composOp qn4rtl p

-- TODO problem with in-situ quantification! Maybe leave out ltr of qd1 and qd2?
-- Quantifier distribution 1: (\forall x) (phi(x) \& \psi(x)) <-> (\forall x) (phi(x)) \& (\forall x) (psi(x))
quantdist1ltr :: GProp -> GProp
quantdist1ltr = qd1ltr
qd1ltr :: forall c. Tree c -> Tree c
qd1ltr p = case p of
  GPUniv v1 (GPConj GCAnd p1 p2) | v1 `elem` (freeVars p1) && v1 `elem` (freeVars p2) 
    -> GPConj GCAnd (GPUniv v1 p1) (GPUniv v1 p2)
  _ -> composOp qd1ltr p

quantdist1rtl :: GProp -> GProp
quantdist1rtl = qd1rtl
qd1rtl :: forall c. Tree c -> Tree c
qd1rtl p = case p of
  GPConj GCAnd (GPUniv v1 p1) (GPUniv v2 p2) | v1 == v2 && v1 `elem` (freeVars p1) && v1 `elem` (freeVars p2) 
    -> GPUniv v1 (GPConj GCAnd p1 p2)
  _ -> composOp qd1rtl p

-- Quantifier distribution 2: (\exists x) (phi(x) \vee \psi(x)) <-> (\exists x) (phi(x)) \vee (\exists x) (psi(x))
quantdist2ltr :: GProp -> GProp
quantdist2ltr = qd2ltr
qd2ltr :: forall c. Tree c -> Tree c
qd2ltr p = case p of
  GPExist v1 (GPConj GCOr p1 p2) | v1 `elem` (freeVars p1) && v1 `elem` (freeVars p2) 
    -> GPConj GCOr (GPExist v1 p1) (GPExist v1 p2)
  _ -> composOp qd2ltr p

quantdist2rtl :: GProp -> GProp
quantdist2rtl = qd2rtl
qd2rtl :: forall c. Tree c -> Tree c
qd2rtl p = case p of
  GPConj GCOr (GPExist v1 p1) (GPExist v2 p2) | v1 == v2 && v1 `elem` (freeVars p1) && v1 `elem` (freeVars p2) 
    -> GPExist v1 (GPConj GCOr p1 p2)
  _ -> composOp qd2rtl p
  
-- Quantifier distribution 3 (consequence): (\forall x) phi(x) \vee (\forall x) \psi(x)) -> (\forall x) (phi(x) \vee psi(x))
quantdist3 :: GProp -> GProp
quantdist3 = qd3
qd3 :: forall c. Tree c -> Tree c
qd3 p = case p of
  GPConj GCOr (GPUniv v1 p1) (GPUniv v2 p2) | v1 == v2 && v1 `elem` (freeVars p1) && v1 `elem` (freeVars p2) 
    -> GPUniv v1 (GPConj GCOr p1 p2)
  _ -> composOp qd3 p
  
-- Quantifier distribution 4 (consequence): (\exists x) (phi(x) \& \psi(x)) -> (\exists x) phi(x) \& (\exists x) psi(x)
quantdist4 :: GProp -> GProp
quantdist4 = qd4
qd4 :: forall c. Tree c -> Tree c
qd4 p = case p of
  GPExist v1 (GPConj GCAnd p1 p2) | v1 `elem` (freeVars p1) && v1 `elem` (freeVars p2) 
    -> GPConj GCAnd (GPExist v1 p1) (GPExist v1 p2)
  _ -> composOp qd4 p
  
-- Quantifier independence 1 (ltr and rtl are the same): (\forall x) (\forall y) phi(x,y) <-> (\forall y) (\forall x) phi(x,y)
quantind1 :: GProp -> GProp
quantind1 = qi1
qi1 :: forall c. Tree c -> Tree c
qi1 p = case p of
  GPUniv v1 (GPUniv v2 p1) | v1 `elem` (freeVars p1) && v2 `elem` (freeVars p1) 
    -> GPUniv v2 (GPUniv v1 p1)
  _ -> composOp qi1 p
  
-- Quantifier independence 2 (ltr and rtl are the same): (\exists x) (\exists y) phi(x,y) <-> (\exists y) (\exists x) phi(x,y)
quantind2 :: GProp -> GProp
quantind2 = qi2
qi2 :: forall c. Tree c -> Tree c
qi2 p = case p of
  GPExist v1 (GPExist v2 p1) | v1 `elem` (freeVars p1) && v2 `elem` (freeVars p1) 
    -> GPExist v2 (GPExist v1 p1)
  _ -> composOp qi2 p
  
-- Quantifier independence 3 (consequence): (\exists x) (\forall y) phi(x,y) -> (\forall y) (\exists x) phi(x,y)
quantind3 :: GProp -> GProp
quantind3 = qi3
qi3 :: forall c. Tree c -> Tree c
qi3 p = case p of
  GPExist v1 (GPUniv v2 p1) | v1 `elem` (freeVars p1) && v2 `elem` (freeVars p1) 
    -> GPUniv v2 (GPExist v1 p1)
  _ -> composOp qi3 p
  
-- Quantifier movement 1: phi \supset (\forall x) psi(x) <-> (\forall x) (phi \supset psi(x))
quantmov1ltr :: GProp -> GProp
quantmov1ltr = qm1ltr
qm1ltr :: forall c. Tree c -> Tree c
qm1ltr p = case p of
  GPImpl p1 (GPUniv v1 p2) | v1 `elem` (freeVars p2)
    -> GPUniv v1 (GPImpl p1 p2)
  _ -> composOp qm1ltr p
  
quantmov1rtl :: GProp -> GProp
quantmov1rtl = qm1rtl
qm1rtl :: forall c. Tree c -> Tree c
qm1rtl p = case p of
  GPUniv v1 (GPImpl p1 p2) | v1 `elem` (freeVars p2)
    -> GPImpl p1 (GPUniv v1 p2)
  _ -> composOp qm1rtl p
  
-- Quantifier movement 2: phi \supset (\exists x) psi(x) <-> (\exists x) (phi \supset psi(x))
quantmov2ltr :: GProp -> GProp
quantmov2ltr = qm2ltr
qm2ltr :: forall c. Tree c -> Tree c
qm2ltr p = case p of
  GPImpl p1 (GPExist v1 p2) | v1 `elem` (freeVars p2)
    -> GPExist v1 (GPImpl p1 p2)
  _ -> composOp qm2ltr p
  
quantmov2rtl :: GProp -> GProp
quantmov2rtl = qm2rtl
qm2rtl :: forall c. Tree c -> Tree c
qm2rtl p = case p of
  GPExist v1 (GPImpl p1 p2) | v1 `elem` (freeVars p2)
    -> GPImpl p1 (GPExist v1 p2)
  _ -> composOp qm2rtl p
  
-- Quantifier movement 3: (\forall x) phi(x) \supset psi <-> (\exists x) (phi(x) \supset psi)
quantmov3ltr :: GProp -> GProp
quantmov3ltr = qm3ltr
qm3ltr :: forall c. Tree c -> Tree c
qm3ltr p = case p of
  GPImpl (GPUniv v1 p1) p2 | v1 `elem` (freeVars p1)
    -> GPExist v1 (GPImpl p1 p2)
  _ -> composOp qm3ltr p
  
quantmov3rtl :: GProp -> GProp
quantmov3rtl = qm3rtl
qm3rtl :: forall c. Tree c -> Tree c
qm3rtl p = case p of
  GPExist v1 (GPImpl p1 p2) | v1 `elem` (freeVars p1)
    -> GPImpl (GPUniv v1 p1) p2
  _ -> composOp qm3rtl p
  
-- Quantifier movement 4: (\exists x) phi(x) \supset psi <-> (\forall x) (phi(x) \supset psi)
quantmov4ltr :: GProp -> GProp
quantmov4ltr = qm4ltr
qm4ltr :: forall c. Tree c -> Tree c
qm4ltr p = case p of
  GPImpl (GPExist v1 p1) p2 | v1 `elem` (freeVars p1)
    -> GPUniv v1 (GPImpl p1 p2)
  _ -> composOp qm4ltr p
  
quantmov4rtl :: GProp -> GProp
quantmov4rtl = qm4rtl
qm4rtl :: forall c. Tree c -> Tree c
qm4rtl p = case p of
  GPUniv v1 (GPImpl p1 p2) | v1 `elem` (freeVars p1)
    -> GPImpl (GPExist v1 p1) p2
  _ -> composOp qm4rtl p
  
-- Vacuous quantification 1: (\forall x) phi <-> phi
vacquant1 :: GProp -> GProp
vacquant1 = vq1
vq1 :: forall c. Tree c -> Tree c
vq1 p = case p of
  GPUniv v1 p1 | not (v1 `elem` (freeVars p1)) -> p1
  _ -> composOp vq1 p
  
-- Vacuous quantification 2: (\exists x) phi <-> phi
vacquant2 :: GProp -> GProp
vacquant2 = vq2
vq2 :: forall c. Tree c -> Tree c
vq2 p = case p of
  GPExist v1 p1 | not (v1 `elem` (freeVars p1)) -> p1
  _ -> composOp vq2 p
  
-- TODO Do not forget alphabetic variants!!

  
