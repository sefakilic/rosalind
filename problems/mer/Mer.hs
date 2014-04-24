-- http://rosalind.info/problems/mer/

import Data.List
import Data.List.Split

merge :: [Int] -> [Int] -> [Int]
merge [] ys = ys
merge xs [] = xs
merge xs'@(x:xs) ys'@(y:ys)
  | x < y     = x:(merge xs ys')
  | otherwise = y:(merge xs' ys)

main :: IO ()
main = do
  ln <- getLine                 -- read n
  ln <- getLine                 -- read n numbers
  let as = map (\x -> (read x) :: Int) (splitOn " " ln)
  ln <- getLine                 -- read m
  ln <- getLine                 -- read m numbers
  let bs = map (\x -> (read x) :: Int) (splitOn " " ln)

  putStrLn $ intercalate " " (map show (merge as bs))
