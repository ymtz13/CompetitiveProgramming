import Data.Char

toInt = read :: String -> Integer

toggleCase :: Char -> Char
toggleCase c = if isUpper c then toLower c else toUpper c

main = do
  _nk <- getLine
  t <- getLine

  let [n, k] = map toInt (words _nk)
  let ans = zipWith (\i c -> if i < k then c else toggleCase c) [1 ..] t

  putStrLn ans
