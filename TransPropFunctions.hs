{-# LANGUAGE PackageImports #-}
{-# LANGUAGE GADTs #-}
{-# OPTIONS_GHC -fglasgow-exts #-}

module TransPropFunctions where

import qualified "gf" PGF (Tree, showExpr)
import Prop   -- generated from GF
import Data.List (minimumBy)
import Data.Ord (comparing)

-- Useful functions
-- Ranta 2011 (moved from TransProp.hs)
noFreeVars :: PGF.Tree -> Bool
noFreeVars = null . freeVarsP . fg
  where
    freeVarsP :: GProp -> [GVar]
    freeVarsP = freeVars

getPred1s :: [GProp] -> Maybe ([GPred1],[GInd])
getPred1s = fmap unzip . mapM getPred1 where
  getPred1 :: GProp -> Maybe (GPred1,GInd)
  getPred1 p = case p of
    GPAtom (GAPred1 f x)   -> return (f,x)
    _ -> Nothing
    
-- Elze: for aggregPred2
getPred2s :: [GProp] -> Maybe ([GPred2],[(GInd, GInd)])
getPred2s = fmap unzip . mapM getPred2 where
  getPred2 :: GProp -> Maybe (GPred2,(GInd, GInd))
  getPred2 p = case p of
    GPAtom (GAPred2 f x y) -> return (f, (x,y))
    GPAtom (GAPredColl f (GListInd xs)) | length xs == 2 -> return (f, ((xs !! 0), (xs !! 1)))
    _ -> Nothing
    
freeVars :: Tree a -> [GVar]
freeVars t = [x | x@(GVString _) <- freeVarsM t]
 where
  freeVarsM :: forall a. Tree a -> [GVar]
  freeVarsM t = case t of
    GPUniv x p -> filter (/= x) $ freeVarsM p
    GPExist x p -> filter (/= x) $ freeVarsM p
    GPUnivs (GListVar xs) k p -> freeVarsM k ++ filter (flip notElem xs) (freeVarsM p)
    GPExists (GListVar xs) k p -> freeVarsM k ++ filter (flip notElem xs) (freeVarsM p)
    GVString _ -> [t]
    _ -> composOpMPlus freeVarsM t

notFree :: GVar -> Tree a -> Bool
notFree x t = notElem x (freeVars t)

-- Elze
--Find the shortest sentence in a list of sentences (by word count)
shortestSentence :: [String] -> String
shortestSentence l = minimumBy (comparing wordCount) l

wordCount :: String -> Int
wordCount s = length (filter (/= ",") (words s)) -- TODO other punctuation marks to ignore?

getProps :: Tree a -> [GProp]
getProps t = [p | p <- propsM t]
 where
  propsM :: forall a. Tree a -> [GProp]
  propsM t = case t of
    GPTaut -> [t]
    GPContra -> [t]
    _ -> composOpMPlus propsM t

--TODO remove?   
--containsTorF :: GProp -> Bool
--containsTorF p = GPTaut `elem` (getProps p) || GPContra `elem` (getProps p)