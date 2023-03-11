mod = 998244353

M = 10**6

F = [1]
for i in range(1, M):
  F.append(F[-1] * i % mod)

Finv = [None] * M
Finv[-1] = pow(F[-1], mod - 2, mod)

for i in range(M - 1, 0, -1):
  Finv[i - 1] = Finv[i] * i % mod


def comb(n, k):
  return F[n] * Finv[n - k] * Finv[k] % mod


N, K = map(int, input().split())
A = list(map(int, input().split()))
S = set(A)

mexA = 0
while mexA in S:
  mexA += 1

ans = 0

if mexA > 0:
  ans += comb(K + mexA - 1, K)
  ans %= mod

for k in range(1, K + 1):
  S.add(mexA)
  while mexA in S:
    mexA += 1

  ans += comb(K - k + mexA - 1, K - k)
  ans %= mod

print(ans)
