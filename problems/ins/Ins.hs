-- http://rosalind.info/problems/ins/

import Data.List
import Data.List.Split

-- number of swaps performed during insertion sort
insertionSortSwaps :: [Int] -> Int
insertionSortSwaps xs = snd $ foldl f ([], 0) xs
  where f (sorted, cnt) x = let less = filter (<=x) sorted
                                more = filter (>x) sorted
                            in (less ++ [x] ++ more, cnt + length more)

main :: IO ()
main = do
  _ <- getLine
  ln <- getLine
  let nums = map (\x -> (read x) :: Int) (splitOn " " ln)
  print $ insertionSortSwaps nums


