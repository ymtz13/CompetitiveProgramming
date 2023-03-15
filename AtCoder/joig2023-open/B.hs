toInt = read :: String -> Integer

main = do
  _n <- getLine
  _as <- getLine

  let n = toInt _n
  let as = map toInt $ words _as

  print $ head $ solve as

solve :: [Integer] -> [Integer]
solve as
  | length as == 1 = as
  | otherwise = solve $ zipWith (\x y -> abs (x - y)) (tail as) as
