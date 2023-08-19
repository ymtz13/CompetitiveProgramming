from collections import defaultdict

mod = 998244353

F = [1]
for i in range(1, 5000):
    F.append(F[-1] * i % mod)

Finv = [None] * len(F)
Finv[-1] = pow(F[-1], mod - 2, mod)
for i in range(len(F) - 1, 0, -1):
    Finv[i - 1] = Finv[i] * i % mod


def comb(n, k):
    return F[n] * Finv[k] * Finv[n - k] % mod


N, M, K = map(int, input().split())
A = list(map(int, input().split()))

C = [0] * (M + 1)
for a in A:
    C[a] += 1
c0 = C[0]
s = C[1]

P = [0] * (M + 2)
T = P[1] = pow(M, c0, mod)

for m in range(2, M + 1):
    if s >= K:
        break

    p = 0
    for x in range(min(K - 1 - s, c0) + 1):
        y = c0 - x
        p += comb(c0, x) * pow(m - 1, x, mod) * pow(M - m + 1, y, mod) % mod
        p %= mod

    P[m] = p

    s += C[m]


ans = 0
Tinv = pow(T, mod - 2, mod)
for m in range(1, M + 1):
    p = P[m] - P[m + 1]
    ans += m * p * Tinv % mod
    ans %= mod

print(ans)
