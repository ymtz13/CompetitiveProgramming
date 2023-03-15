import Data.Bits
import Data.List

toInt = read :: String -> Integer

main = do
  _nmk <- getLine
  _as <- getLine
  _bs <- getLine

  let nmk = map toInt $ words _nmk
  let n = head nmk
  let m = head $ tail nmk
  let k = last nmk

  let as = map toInt $ words _as
  let bs = map toInt $ words _bs

  putStr $ unlines $ map show $ solve m k as bs

pinf = shift 1 60 :: Integer

ninf = -pinf :: Integer

-- solve :: Integer -> [Integer] -> [Integer] -> [Integer]

solve m k as bs = ans
  where
    mplus1 = m + 1

    asTagged = map (* mplus1) as
    bsTagged = zipWith (\x i -> x * mplus1 + i) bs [1 ..]

    ms = sort $ asTagged ++ bsTagged

    sound d = max 0 (k - abs d)

    scan :: [Integer] -> Integer -> [(Integer, Integer)] -> [(Integer, Integer)]
    scan ms xLastBell ret
      | null ms = reverse ret
      | tag == 0 = scan (tail ms) x ret
      | otherwise = scan (tail ms) xLastBell ((sound (x - xLastBell), tag) : ret)
      where
        v = head ms
        x = quot v mplus1
        tag = mod v mplus1

    scanl = scan ms ninf []
    scanr = scan (reverse ms) pinf []

    ans = map fst $ sortOn snd $ zipWith max scanl (reverse scanr)
