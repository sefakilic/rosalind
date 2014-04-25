import Data.List
import Data.Maybe
import Control.Monad

_2sum :: [Int] -> Maybe (Int, Int)
_2sum xs = if not (null matches)
           then Just (head matches)
           else Nothing
  where matches = [(i, i+(fromJust j)+1) | i <- [1..length xs],
                   let j = elemIndex (-(xs !! (i-1))) (drop i xs),
                   j /= Nothing]

printVal :: Maybe (Int, Int) -> IO ()
printVal (Just (x,y)) = putStrLn $ show x ++ " " ++ show y
printVal Nothing      = putStrLn "-1"
                   


main = do
  ln <- getLine
  let (k:n:_) = map (\x -> (read x) :: Int) (words ln)
  forM [1..k] (\_ -> do
                  ln <- getLine
                  let nums = map (\x -> (read x) :: Int) (words ln)
                  printVal $ _2sum nums)
  return ()
