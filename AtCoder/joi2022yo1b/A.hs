toInt = read :: String -> Integer

main = do
  _x <- getLine
  let x = toInt _x

  print $ x * x * x
