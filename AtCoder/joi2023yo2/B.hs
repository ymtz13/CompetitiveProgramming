import Data.Bits
import Data.List

pinf = shift 1 60

toInt = read :: String -> Integer

main = do
  _n <- getLine
  _as <- getLine
  _bs <- getLine
  _cs <- getLine
  _ds <- getLine

  let as = map toInt $ words _as
  let bs = map toInt $ words _bs
  let cs = map toInt $ words _cs
  let ds = map toInt $ words _ds

  print $ solve as bs cs ds

solve as bs cs ds = go as' bs' cs' ds'
  where
    go as@(a : as') bs@(b : bs') cs@(c : cs') ds@(d : ds')
      | null as' && null bs' && null cs' && null ds' = pinf
      | vmin == a = min diff (go as' bs cs ds)
      | vmin == b = min diff (go as bs' cs ds)
      | vmin == c = min diff (go as bs cs' ds)
      | vmin == d = min diff (go as bs cs ds')
      where
        vmin = minimum [a, b, c, d]
        vmax = maximum [a, b, c, d]
        diff = vmax - vmin

    as' = sort (pinf : as)
    bs' = sort (pinf * 2 : bs)
    cs' = sort (pinf * 3 : cs)
    ds' = sort (pinf * 4 : ds)
