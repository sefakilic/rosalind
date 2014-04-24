-- http://rosalind.info/problems/med/

-- Find the smallest kth element (without sorting)

import Data.List
import Data.List.Split

randomNumber :: Int
randomNumber = 0                -- chosen by fair dice roll.
                                -- guaranteed to be random.
                                -- http://xkcd.com/221/

med :: [Int] -> Int -> Int
med xs k
  | k <= l            = med less k
  | l < k && k <= l+e = head equal
  | otherwise         = med more (k-l-e)
  where rnd = xs !! randomNumber
        less = filter (<rnd) xs
        equal = filter (==rnd) xs
        more = filter (>rnd) xs
        l = length less
        e = length equal
        m = length more

main :: IO ()
main = do
  _ <- getLine
  ln <- getLine
  let nums = map (\x -> (read x) :: Int) (splitOn " " ln)
  ln <- getLine
  let k = (read ln) :: Int
  print $ med nums k
