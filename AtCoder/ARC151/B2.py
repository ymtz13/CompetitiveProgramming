N, M = map(int, input().split())
P = list(map(int, input().split()))

L = [None] * (N + 1)
for i, p in enumerate(P):
  L[p] = i

ans = 0
mod = 998244353
X = (M - 1) * M // 2
for i in range(N - 1):
  if i + 1 != P[i]:
    ans += X * pow(M, N - i - 2, mod)
    ans %= mod

  P[L[i + 1]] = P[i]

  print(P)

print(ans)
