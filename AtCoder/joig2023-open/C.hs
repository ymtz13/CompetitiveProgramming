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

  putStr $ unlines $ map show $ solve k as bs

pinf = shift 1 60 :: Integer

ninf = -pinf :: Integer

-- solve :: Integer -> [Integer] -> [Integer] -> [Integer]

solve k as bs = ans
  where
    bells = [ninf] ++ sort as ++ [pinf]
    houses = sort $ zip bs [1 ..]

    rvBells = map negate $ reverse bells
    rvHouses = map (\(x, i) -> (-x, i)) $ reverse houses

    sound d = max 0 (k - abs d)

    scan :: [Integer] -> [(Integer, Integer)] -> Integer -> [(Integer, Integer)] -> [(Integer, Integer)]
    scan bells houses lastBell ret
      | null houses = reverse ret
      | headBell <= headHouse = scan (tail bells) houses headBell ret
      | otherwise = scan bells (tail houses) lastBell ((headHouseIndex, sound (headHouse - lastBell)) : ret)
      where
        headBell = head bells
        (headHouse, headHouseIndex) = head houses

    scanl = scan bells houses 0 []
    scanr = scan rvBells rvHouses 0 []

    ans = map snd $ sort $ zipWith max scanl (reverse scanr)
