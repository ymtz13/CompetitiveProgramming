toInt = read :: String -> Integer

main = do
  _n <- getLine
  let n = toInt _n
  print $ n * 24
