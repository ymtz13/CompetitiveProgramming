from mod import Mod

mod1b7 = Mod(10**9 + 7, 30)

assert mod1b7.comb(8, 0) == 1
assert mod1b7.comb(8, 1) == 8
assert mod1b7.comb(8, 2) == 28
assert mod1b7.comb(8, 3) == 56
assert mod1b7.comb(8, 4) == 70

mod11 = Mod(11, 10)

assert mod11.factorial[5] == 10
