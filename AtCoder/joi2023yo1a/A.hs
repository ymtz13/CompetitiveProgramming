toInt = read :: String -> Integer

main = do
  _a <- getLine
  _b <- getLine

  let a = toInt _a
  let b = toInt _b

  print $ a * b
