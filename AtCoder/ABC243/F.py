mod = 998244353


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

    def comb(self, n, k):
        return (
            self.factorial[n]
            * self.factorial_inv[n - k]
            * self.factorial_inv[k]
            % self.mod
        )


mmod = Mod(mod, 120)

N, M, K = map(int, input().split())
W = [int(input()) for _ in range(N)]

S = sum(W)
Sinv = pow(S, mod - 2, mod)
P = [w * Sinv % mod for w in W]
# Sinv = 1 / S
# P = [w * Sinv for w in W]

if N == 1:
    print(1)
    exit()

if M > K:
    print(0)
    exit()

K1 = K + 1

dp = [0] * (K1 * K1)
dp[0] = 1

for p in P:
    for n in range(K, 0, -1):
        for m in range(1, n + 1):
            t = m * K1 + n
            for c in range(1, n + 1):
                f = n - c
                k = mmod.comb(K - f, c)
                l = pow(p, c, mod)

                dp[t] += dp[(m - 1) * K1 + f] * k * l % mod
                dp[t] %= mod

print(dp[M * K1 + K])
