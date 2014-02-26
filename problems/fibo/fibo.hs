-- http://rosalind.info/problems/fibo/

-- run: runghc fibo.hs < rosalind_fibo.txt

fibo 0 = 0
fibo 1 = 1
fibo n = fibo (n-1) + fibo (n-2)

main = do
  n <- getLine
  print (fibo (read n :: Int))
  