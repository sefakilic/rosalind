-- http://rosalind.info/problems/maj/ 

import Data.List.Split
import Data.List
import Control.Monad

maj :: [Int] -> Int
maj xs = f $ filter (\g -> length g > (length xs) `quot` 2) (group $ sort xs)
  where f (xs:_) = head xs
        f []    = -1

toInt :: String -> Int
toInt x = (read x) :: Int

main :: IO ()
main = do
  ln <- getLine
  let k:n:_ = map toInt (splitOn " " ln)
  forM_ [1..k] (\_ -> do
                   ln <- getLine
                   putStr $ show $ maj (map toInt (splitOn " " ln))
                   putStr " ")
  putStrLn ""
    
