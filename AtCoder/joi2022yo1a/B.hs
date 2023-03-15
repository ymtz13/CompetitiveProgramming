toInt = read :: String -> Integer

main = do
  _x <- getLine
  _y <- getLine
  _z <- getLine

  let x = toInt _x
  let y = toInt _y
  let z = toInt _z
  print $ if x + y <= z then 1 else 0
