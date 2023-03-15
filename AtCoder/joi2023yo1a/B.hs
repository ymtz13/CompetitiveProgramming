main = do
  n <- getLine

  print $ if head n == last n then 1 else 0
