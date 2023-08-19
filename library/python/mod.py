class Mod:
    def __init__(self, mod, fMax):
        F = [1]
        for n in range(1, fMax + 10):
            F.append(F[-1] * n % mod)

        Finv = [pow(F[-1], mod - 2, mod)]
        for n in range(len(F) - 1, 0, -1):
            Finv.append(Finv[-1] * n % mod)
        Finv.reverse()

        self.mod = mod
        self.fMax = fMax
        self.F = F
        self.Finv = Finv

    def comb(self, n, k):
        return self.F[n] * self.Finv[n - k] * self.Finv[k] % self.mod


mod = Mod(10**9 + 7, 30)

assert mod.comb(8, 0) == 1
assert mod.comb(8, 1) == 8
assert mod.comb(8, 2) == 28
assert mod.comb(8, 3) == 56
assert mod.comb(8, 4) == 70
