class Mod:
    def __init__(self, mod, fMax):
        factorial = [1]
        for n in range(1, fMax + 10):
            factorial.append(factorial[-1] * n % mod)

        factorial_inv = [pow(factorial[-1], mod - 2, mod)]
        for n in range(len(factorial) - 1, 0, -1):
            factorial_inv.append(factorial_inv[-1] * n % mod)
        factorial_inv.reverse()

        self.mod = mod
        self.fMax = fMax
        self.factorial = factorial
        self.factorial_inv = factorial_inv

    def binom(self, n, k):
        return (
            self.factorial[n]
            * self.factorial_inv[n - k]
            * self.factorial_inv[k]
            % self.mod
        )


mod = 998244353

N, K = map(int, input().split())
S = input()

m = Mod(mod, N + 10)

nA = S.count("A")
nB = S.count("B")
nC = S.count("C")

ans = 0

for rBCA in range(K // 2 + 1):
    for mBA in range(K - rBCA * 2 + 1):
        for mCB in range(K - rBCA * 2 - mBA + 1):
            for mAC in range(K - rBCA * 2 - mBA - mCB + 1):
                mAB = rBCA + mBA
                mBC = rBCA + mCB
                mCA = rBCA + mAC

                Ain = mBA + mCA
                Bin = mAB + mCB
                Cin = mAC + mBC

                if Ain > nA:
                    continue
                if Bin > nB:
                    continue
                if Cin > nC:
                    continue

                p = 1
                p = p * m.binom(nA, mAB) * m.binom(nA - mAB, mAC) % mod
                p = p * m.binom(nB, mBA) * m.binom(nB - mBA, mBC) % mod
                p = p * m.binom(nC, mCA) * m.binom(nC - mCA, mCB) % mod

                ans += p
                ans %= mod

for rCAB in range(1, K // 2 + 1):
    for mCA in range(K - rCAB * 2 + 1):
        for mAB in range(K - rCAB * 2 - mCA + 1):
            for mBC in range(K - rCAB * 2 - mCA - mAB + 1):
                mAC = rCAB + mCA
                mBA = rCAB + mAB
                mCB = rCAB + mBC

                Ain = mBA + mCA
                Bin = mAB + mCB
                Cin = mAC + mBC

                if Ain > nA:
                    continue
                if Bin > nB:
                    continue
                if Cin > nC:
                    continue

                p = 1
                p = p * m.binom(nA, mAB) * m.binom(nA - mAB, mAC) % mod
                p = p * m.binom(nB, mBA) * m.binom(nB - mBA, mBC) % mod
                p = p * m.binom(nC, mCA) * m.binom(nC - mCA, mCB) % mod

                ans += p
                ans %= mod


print(ans)
