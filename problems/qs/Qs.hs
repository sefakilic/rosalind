import Data.List
import Data.List.Split
import Control.Monad

qs :: Ord a => [a] -> [a]
qs [] = []
qs (x:xs) = qs left ++ [x] ++ qs right
  where left = filter (<x) xs
        right = filter (>=x) xs

main :: IO ()
main = do
  _ <- getLine
  ln <- getLine
  let nums = map (\x -> (read x) :: Int) (splitOn " " ln)
  putStrLn $ intercalate " " (map show $ qs nums)
