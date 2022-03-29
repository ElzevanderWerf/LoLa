{-# LANGUAGE PackageImports #-}
module Main where

import "gf" PGF
import TransProp

main = do
  pgf <- readPGF "Prop.pgf"
  interact (doTrans pgf)

--doTrans pgf s = case parseAllLang pgf (startCat pgf) s of 
--  (l,ts):_ -> unlines [display m l u | t <- ts, noFreeVars t, (u,m) <- transfers t]
--  _ -> "no parse\n"
-- where
--   display m l u = unlines $ (show m ++ ":") : 
--     showExpr [] u : [s | la <- languages pgf, let s = linearize pgf la u]
--   transfers t = [(transfer m t,m) | m <- [MNone, MOptimize, MNormalize, MMinimalize]
   
doTrans pgf s = case parseAllLang pgf (startCat pgf) s of 
  (sourceL,ts):_ -> unlines [display sourceL transl | t <- ts, noFreeVars t, transl <- linearize pgf la resultTree, la <- languages pgf, resultTree <- simplifyP t la]
  _ -> "no parse\n"
 where
   display l u = unlines $ (show l ++ ":") : 
     showExpr [] u : [s | la <- languages pgf, let s = linearize pgf la u]