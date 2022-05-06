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
    else do                -- stack run trans <mode> <source-language> <input-file> <target-language> <output-file>
      f <- readFile (args !! 2)
      let flines = lines f
      let mode = args !! 0
      let sourcelang = mkCId (args !! 1)
      let targetlang = mkCId (args !! 3)
      
      -- Translate and write to output file
      outh <- openFile (args !! 4) WriteMode
      let doTransPGF = doTransFromTo pgf mode sourcelang targetlang
      hPutStrLn outh (unlines (map doTransPGF flines))
      hClose outh

      putStrLn "done"
    
-- Parse the input string in all languages and translate it with all 
-- translation modes into all languages 
doTrans pgf s = case parseAllLang pgf (startCat pgf) s of 
  (sourceL,ts):_ -> unlines [display m t | t <- ts, m <- [MNone, MOptimize, MNormalize, MMinimalize, MSimplify, MCheckLaw]] 
  _              -> "no parse\n"
 where
   display m t = unlines $ (showExpr [] t) :           -- print the tree
       (show m ++ ":") :                               -- print the mode
         [transfer m pgf la t | la <- languages pgf]   -- print the translations (for each language)

-- Parse the input string in the source language and translate it with
-- AST simplification into the target language
doTransFromTo pgf mode source_l target_l s = case parse pgf source_l (startCat pgf) s of 
  ts | length ts > 0 -> unlines [wb t ++ transfers t | t <- ts]    -- this assumes the input sentences are parsable
   where
     wb t = if (isWellBehaved t) then "WB, " else "NWB, "   -- check well-behavedness
     transfers t = case mode of
       "MNone" -> transferss MNone
       "MOptimize" -> transferss MOptimize
       "MNormalize" -> transferss MNormalize
       "MMinimalize" -> transferss MMinimalize
       "MSimplify" -> transferss MSimplify
      where
        transferss m = transfer m pgf target_l t
  _  -> "no parse"