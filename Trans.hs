{-# LANGUAGE PackageImports #-}
module Main where

import "gf" PGF
import TransProp
import TransPropFunctions

main = do
  pgf <- readPGF "Prop.pgf"
  interact (doTrans pgf)     -- translate the input proposition

-- Parse the input string in all languages and translate it with all 
-- translation modes into all languages 
doTrans pgf s = case parseAllLang pgf (startCat pgf) s of 
  (sourceL,ts):_ -> unlines [display m t | t <- ts, noFreeVars t, m <- [MNone, MOptimize, MNormalize, MMinimalize, MSimplify, MCheckLaw]] 
  --(sourceL,ts):_ -> unlines [display m t | t <- ts, noFreeVars t, m <- [MSimplify]] --Debug: print tree
  _ -> "no parse\n"
 where
   display m t = unlines $ (showExpr [] t) :                 -- print the tree
     (show m ++ ":") :                                       -- print the mode
       [transfer m pgf la t | la <- languages pgf]           -- print the translations (for each language)
       --[unlines (map show (transfer m pgf la t)) | la <- languages pgf]      -- Debug: print tree