import Data.Maybe
import Data.List

massTable = [
  ('G', 57),
  ('A', 71),
  ('S', 87),
  ('P', 97),
  ('V', 99),
  ('T', 101),
  ('C', 103),
  ('I', 113),
  ('L', 113),
  ('N', 114),
  ('D', 115),
  ('K', 128),
  ('Q', 128),
  ('E', 129),
  ('M', 131),
  ('H', 137),
  ('F', 147),
  ('R', 156),
  ('Y', 163),
  ('W', 186)]
            
mass :: String -> Int            
mass [] = 0
mass (x:xs) = (fromJust $ lookup x massTable) + (mass xs)

-- all substrings of length n of a circular string
ncycle :: [a] -> Int -> [[a]]
ncycle xs n 
  | length xs == n = [xs]
  | otherwise = [take n (drop i $ cycle xs) | i <- [0..(length xs)-1]]

cyclospectrum :: String -> [Int]
cyclospectrum xs = sort (0:[res | n <- [1..length xs], res <- aux xs n])
  where aux xs n = map mass (ncycle xs n)
                                               
main :: IO()
main = do
  aa <- getLine
  putStrLn $ intercalate " " (map show $ cyclospectrum aa)
  