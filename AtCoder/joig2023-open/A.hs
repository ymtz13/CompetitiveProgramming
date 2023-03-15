main = do
  _ <- getLine
  s <- getLine

  putStrLn $ solve s

solve :: String -> String
solve s = if last s == 'G' then init s else s ++ "G"
