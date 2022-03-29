{-# LANGUAGE PackageImports #-}
{-# LANGUAGE GADTs #-}
{-# OPTIONS_GHC -fglasgow-exts #-}

module LogicLaws where

import qualified "gf" PGF (Tree, showExpr)
import Prop   -- generated from GF

-- List of two-way logical equivalences



-- List of one-way logical equivalences and logical consequences
-- (The "one-way" logical equivalences work both ways, 
-- but can shorten the formula in only one direction)
-- Idempotence 1: p \vee p -> p
idempotence1 :: GProp -> GProp
idempotence1 = ip1

ip1 :: forall c. Tree c -> Tree c
ip1 t = case t of
  GPConj GCOr p1 p2 | p1 == p2 -> p1
  _ -> composOp ip1 t
  

-- Complement 2 (double negation): \neg \neg p -> p 
complement2 :: GProp -> GProp
complement2 = comp2

comp2 :: forall c. Tree c -> Tree c
comp2 t = case t of
  GPNeg (GPNeg p) -> p
  GPNeg (GPNegAtom a) -> GPAtom a 
  _ -> composOp comp2 t