toInt = read :: String -> Integer

main = do
  _a <- getLine
  _b <- getLine

  let a = toInt _a
  let b = toInt _b

  print $ solve a b
  where
    solve a b | a < b = -1 | a > b = 1 | otherwise = 0
