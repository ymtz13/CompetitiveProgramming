toInt = read :: String -> Integer

main = do
  x <- getLine
  print $ mod (toInt x) 21
