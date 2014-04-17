module Main where

import RosalindUtils



main = do
  l <- readIntList
  let [k,n] = l
  majs <- forM [1..k] (\a -> do
                          l <- readIntList
                          return (majority l))
  intercalate " " (map show majs)

