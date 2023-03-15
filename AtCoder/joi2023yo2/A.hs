toInt = read :: String -> Integer

main = do
  _n <- getLine
  _as <- getLine

  let n = toInt _n
  let as = map toInt $ words _as

  putStr $ unlines $ map show $ solve n as

solve :: Integer -> [Integer] -> [Integer]
solve n as = map go as
  where
    go :: Integer -> Integer
    go x = max (amax - x) (x - amin)

    amax, amin :: Integer
    amax = foldl max (head as) as
    amin = foldl min (head as) as
