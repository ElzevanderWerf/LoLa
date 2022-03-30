{-# LANGUAGE PackageImports #-}
{-# LANGUAGE GADTs #-}
{-# OPTIONS_GHC -fglasgow-exts #-}

module LogicLaws where

import qualified "gf" PGF (Tree, showExpr)
import Prop   -- generated from GF

logicLaws = [associativity1ltr, associativity1rtl, associativity2ltr, 
  associativity2rtl, commutativity1, commutativity2, distributivity1ltr,
  distributivity1rtl, distributivity2ltr, distributivity2rtl, idempotence1, 
  idempotence2, identity1, identity2, identity3, identity4, complement1,
  complement2, complement3, deMorgan1ltr, deMorgan1rtl, deMorgan2ltr,
  deMorgan2rtl]

-- List of two-way logical equivalences (rtl = right-to-left, ltr = left-to-right)
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
  
-- Commutativity 1: p \vee q <-> q \vee p
commutativity1 :: GProp -> GProp
commutativity1 = comm1
comm1 :: forall c. Tree c -> Tree c
comm1 p = case p of
  GPConj GCOr p1 p2 -> GPConj GCOr p2 p1
  _ -> composOp comm1 p
  
-- Commutativity 2: p \& q <-> q \& p
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


-- List of one-way logical equivalences and logical consequences
-- (The "one-way" logical equivalences work both ways, 
-- but can shorten the formula in only one direction)
-- Idempotence 1: p \vee p <-> p
idempotence1 :: GProp -> GProp
idempotence1 = ip1
ip1 :: forall c. Tree c -> Tree c
ip1 p = case p of
  GPConj GCOr p1 p2 | p1 == p2 -> p1
  _ -> composOp ip1 p
  
-- Idempotence 2: p \& p <-> p
idempotence2 :: GProp -> GProp
idempotence2 = ip2
ip2 :: forall c. Tree c -> Tree c
ip2 p = case p of
  GPConj GCAnd p1 p2 | p1 == p2 -> p1
  _ -> composOp ip1 p
  
-- Identity 1: p \vee F <-> p
identity1 :: GProp -> GProp
identity1 = id1
id1 :: forall c. Tree c -> Tree c
id1 p = case p of
  GPConj GCOr p1 GPContra -> p1
  _ -> composOp id1 p
  
-- Identity 2: p \vee T <-> T
identity2 :: GProp -> GProp
identity2 = id2
id2 :: forall c. Tree c -> Tree c
id2 p = case p of
  GPConj GCOr p1 GPTaut -> GPTaut
  _ -> composOp id2 p
  
-- Identity 3: p \& F <-> F
identity3 :: GProp -> GProp
identity3 = id3
id3 :: forall c. Tree c -> Tree c
id3 p = case p of
  GPConj GCAnd p1 GPContra -> GPContra
  _ -> composOp id3 p
  
-- Identity 4: p \& T <-> p
identity4 :: GProp -> GProp
identity4 = id4
id4 :: forall c. Tree c -> Tree c
id4 p = case p of
  GPConj GCAnd p1 GPTaut -> p1
  _ -> composOp id4 p
  
-- Complement 1: p \vee \sim p <-> T
complement1 :: GProp -> GProp
complement1 = comp1
comp1 :: forall c. Tree c -> Tree c
comp1 p = case p of
  GPConj GCOr p1 (GPNeg p2) | p1 == p2 -> GPTaut
  GPConj GCOr (GPAtom a1) (GPNegAtom a2) | a1 == a2 -> GPTaut
  _ -> composOp comp2 p
  
-- Complement 2 (double negation): \sim \sim p <-> p 
complement2 :: GProp -> GProp
complement2 = comp2
comp2 :: forall c. Tree c -> Tree c
comp2 p = case p of
  GPNeg (GPNeg p1) -> p1
  GPNeg (GPNegAtom a) -> GPAtom a 
  _ -> composOp comp2 p
  
-- Complement 3: p \& \sim p <-> F
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
  _ -> composOp dm2rtl p