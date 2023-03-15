toInt = read :: String -> Integer

main = do
  _a <- getLine
  _b <- getLine

  let a = toInt _a
  let b = toInt _b
  let c = mod (a + b) 12

  print $ if c == 0 then 12 else c
