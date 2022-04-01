{-# LANGUAGE PackageImports #-}
module Main where

import "gf" PGF
import TransProp
import TransPropFunctions

main = do
  pgf <- readPGF "Prop.pgf"
  interact (doTrans pgf)
  
doTrans pgf s = case parseAllLang pgf (startCat pgf) s of 
  (sourceL,ts):_ -> unlines [display m t | t <- ts, noFreeVars t, m <- [MNone, MOptimize, MNormalize, MMinimalize, MSimplify, MCheckLaw]]
  _ -> "no parse\n"
 where
   display m t = unlines $ (showExpr [] t) :               -- print the tree
     (show m ++ ":") :                                     -- print the mode
       [show (transfer m pgf la t) | la <- languages pgf]  -- print the translations (for each language)
   
-- TODOs: 
-- Some characters are displayed as unicode numbers, is that okay?
-- Find a way to print the tree of possible simplification sequences. Bc I found a problem:
--   p & (q or -q) is not simplified to p 