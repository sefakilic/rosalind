-- http://rosalind.info/problems/par/
import Data.List
import Data.List.Split

par :: [Int] -> [Int]
par (x:xs) = filter (<=x) xs ++ [x] ++ filter (>x) xs

main :: IO ()
main = do
  _ <- getLine
  ln <- getLine
  let nums = map (\x -> (read x) :: Int) (splitOn " " ln)
  putStrLn $ intercalate " " (map show $ par nums)
