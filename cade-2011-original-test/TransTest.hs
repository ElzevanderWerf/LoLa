--- To run this script, do:
--- >stack run trans <source-language> <input-file> <target-language> <output-file>


{-# LANGUAGE PackageImports #-}
module Main where

import "gf" PGF
import TransProp
import System.Environment
import System.IO

main = do
  pgf <- readPGF "Prop.pgf"

  -- Read file
  args <- getArgs
  f <- readFile (args !! 1)
  let flines = lines f

  -- Translate and write to file
  let sourcelang = mkCId (args !! 0)
  let targetlang = mkCId (args !! 2)
  outh <- openFile (args !! 3) WriteMode
  let doTransPGF = doTrans pgf sourcelang targetlang
  hPutStrLn outh (unlines (map doTransPGF flines))
  hClose outh

  -- Done message
  putStrLn "done"

--doTrans :: PGF -> Language -> Language -> String -> String
doTrans pgf from_l to_l s = case parse pgf from_l (startCat pgf) s of 
  ts -> unlines [linearize pgf to_l (transfers t) | t <- ts] -- This assumes the input sentences are parsable!
  -- I removed the noFreeVars check because gr also generates formulas with free variables, and I want them to be translated as well for test 1.
 where
   transfers t = transfer MOptimize t