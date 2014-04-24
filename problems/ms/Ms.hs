-- merge sort
-- http://rosalind.info/problems/ms/

import Data.List
import Data.List.Split

merge :: Ord a => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge xs'@(x:xs) ys'@(y:ys)
  | x < y     = x:(merge xs ys')
  | otherwise = y:(merge xs' ys)
                
mergeSort :: Ord a => [a] -> [a]
mergeSort (x:[]) = [x]
mergeSort xs = merge (mergeSort left) (mergeSort right)
  where (left,right) = splitAt (length xs `div` 2) xs

main :: IO ()
main = do
  _ <- getLine
  ln <- getLine
  let nums = map (\x -> (read x) :: Int) (splitOn " " ln)
  putStrLn $ intercalate " " (map show $ mergeSort nums)
