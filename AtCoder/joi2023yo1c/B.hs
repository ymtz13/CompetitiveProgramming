toInt = read :: String -> Integer

main = do
  _a <- getLine
  _b <- getLine

  let a = toInt _a
  let b = toInt _b

  let x = a + 7 * b

  print (if x <= 30 then 1 else 0)
