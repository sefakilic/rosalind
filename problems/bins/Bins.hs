-- http://rosalind.info/problems/bins/
import Data.List.Split
import Data.List

binarySearch low high xs val 
  | high < low       = -1
  | xs !! mid < val  = binarySearch (mid+1) high xs val
  | xs !! mid > val  = binarySearch low (mid-1) xs val
  | otherwise        = mid+1
  where
    mid = quot (high+low) 2
               
main = do
  -- read n
  inp <- getLine
  let n = read inp :: Int
  -- read m
  inp <- getLine
  let m = read inp :: Int
  -- read arr
  inp <- getLine
  let arr = map (\x -> read x :: Int) (splitOn " " inp)
  -- read keys
  inp <- getLine
  let keys = map (\x -> read x :: Int) (splitOn " " inp)
  let result = map (\val -> binarySearch 0 ((length arr)-1) arr val) keys
  putStrLn $ intercalate " " (map show result)
