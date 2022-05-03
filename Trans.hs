{-# LANGUAGE PackageImports #-}
module Main where

import "gf" PGF
import TransProp
import TransPropFunctions
import System.Environment
import System.IO

main = do
  pgf <- readPGF "Prop.pgf"
  args <- getArgs
  if (length args) == 1    -- stack run trans <proposition>
    then do putStrLn (doTrans pgf (args !! 0))
    else do                -- stack run trans <source-language> <input-file> <target-language> <output-file>
      f <- readFile (args !! 1)
      let flines = lines f
      let sourcelang = mkCId (args !! 0)
      let targetlang = mkCId (args !! 2)
 
      -- Translate and write to output file
      outh <- openFile (args !! 3) WriteMode
      let doTransPGF = doTransFromTo pgf sourcelang targetlang
      hPutStrLn outh (unlines (map doTransPGF flines))
      hClose outh

      putStrLn "done"
    
-- Parse the input string in all languages and translate it with all 
-- translation modes into all languages 
doTrans pgf s = case parseAllLang pgf (startCat pgf) s of 
  (sourceL,ts):_ -> unlines [display m t | t <- ts, noFreeVars t, m <- [MNone, MOptimize, MNormalize, MMinimalize, MSimplify, MCheckLaw]] 
  _              -> "no parse\n"
 where
   display m t = unlines $ (showExpr [] t) :                 -- print the tree
     (show m ++ ":") :                                       -- print the mode
       [transfer m pgf la t | la <- languages pgf]           -- print the translations (for each language)

-- Parse the input string in the source language and translate it with
-- AST simplification into the target language
doTransFromTo pgf source_l target_l s = case parse pgf source_l (startCat pgf) s of 
  ts | length ts > 0 -> unlines [transfers t | t <- ts]    -- TODO add noFreeVars t (this assumes the input sentences are parsable)
   where
     transfers t = 
       if (noFreeVars t) then transfer MSimplify pgf target_l t 
       else "contains free variables"
  _  -> "no parse"