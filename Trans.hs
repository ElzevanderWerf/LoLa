{-# LANGUAGE PackageImports #-}
module Main where

import "gf" PGF
import TransProp
import TransPropFunctions

main = do
  pgf <- readPGF "Prop.pgf"
  interact (doTrans pgf)
  
doTrans pgf s = case parseAllLang pgf (startCat pgf) s of 
  --(sourceL,ts):_ -> unlines [display m t | t <- ts, noFreeVars t, m <- [MNone, MOptimize, MNormalize, MMinimalize, MSimplify, MCheckLaw]]
  (sourceL,ts):_ -> unlines [display m t | t <- ts, noFreeVars t, m <- [MSimplify]]
  _ -> "no parse\n"
 where
   display m t = unlines $ (showExpr [] t) :               -- print the tree
     (show m ++ ":") :                                       -- print the mode
       [unlines (map show (transfer m pgf la t)) | la <- languages pgf]      -- print the translations (for each language)
       --[show (transfer m pgf la t) | la <- languages pgf]  -- print the translations (for each language)

-- TODOs: 
-- Some characters are displayed as unicode numbers, is that okay?
-- See TODOs other files