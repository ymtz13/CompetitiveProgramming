toInt = read :: String -> Integer

main = do
  _a <- getLine

  let [a, b, c] = map toInt $ words _a
  let m = max a (max b c)
  let s = a + b + c

  print $ m * 3 - s
