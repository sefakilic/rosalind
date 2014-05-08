import Data.List
import Data.Maybe
import Control.Monad

-- too slow, booo
_3sum :: [Int] -> Maybe (Int, Int, Int)
_3sum xs = if not (null matches)
           then Just (head matches)
           else Nothing
  where matches = [(i,j,i+j+(fromJust k)+1) | i <- [1..length xs],
                   j <- [i+1..length xs],
                   let k = elemIndex (-(xs!!(i-1) + xs!!(j-1))) (drop j xs),
                   k /= Nothing]
          
printVal :: Maybe (Int, Int, Int) -> IO ()
printVal (Just (x,y,z)) = putStrLn $ show x ++ " " ++ show y ++ " " ++ show z
printVal Nothing        = putStrLn "-1"
                   


main = do
  ln <- getLine
  let (k:n:_) = map (\x -> (read x) :: Int) (words ln)
  forM [1..k] (\_ -> do
                  ln <- getLine
                  let nums = map (\x -> (read x) :: Int) (words ln)
                  printVal $ _3sum nums)
  return ()

