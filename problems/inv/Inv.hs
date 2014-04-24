-- number of inversions in an array
-- http://rosalind.info/problems/inv/

import Data.List.Split

-- this took so long, for n ~ 10^5
numInversions :: Ord a => [a] -> Int
numInversions xs = sum [1 | let n = length xs, i <- [1..n], j <- [1..n],i < j, xs!!(i-1) > xs!!(j-1)]

-- this took so long too, for n ~ 10^5
numInversions' :: Ord a => [a] -> Int
numInversions' (x:[]) = 0
numInversions' (x:xs) = length (filter (<x) xs) + numInversions' xs

-- using merge

                        
main :: IO ()
main = do
  _ <- getLine
  ln <- getLine
  let nums = map (\x -> (read x) :: Int) (splitOn " " ln)
  print $ numInversions' nums
