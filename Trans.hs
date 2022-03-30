{-# LANGUAGE PackageImports #-}
module Main where

import "gf" PGF
import TransProp

main = do
  pgf <- readPGF "Prop.pgf"
  interact (doTrans pgf)
   
doTrans pgf s = case parseAllLang pgf (startCat pgf) s of 
  (sourceL,ts):_ -> unlines [display m ts | m <- [MNone, MOptimize, MNormalize, MMinimalize, MSimplify]]
  _ -> "no parse\n"
 where
   display m ts = unlines $ (show m ++ ":") : [show (transfer m pgf la t) | t <- ts, noFreeVars t, la <- languages pgf]
   
-- TODOs: 
-- Some characters are displayed as unicode numbers, is that okay?
-- Find a way to print the tree of possible simplification sequences