import Data.List
import Data.List.Split

-- Given a list of nodes and edges, return the degree for each node
degree :: [Int] -> [(Int, Int)] -> [Int]
degree ns es = map (\x -> length $ filter (\e -> x == fst e || x == snd e) es) ns

main :: IO ()
main = do
  x <- getContents
  let lns = lines x
      (n:e:_) = map (\x -> (read x) :: Int) (words $ head lns)
      edges = map makeEdge (tail lns)
        where makeEdge ln = let a:b:_ = words ln
                            in ((read a)::Int, (read b)::Int)
  putStrLn $ intercalate " " (map show $ degree [1..n] edges)
