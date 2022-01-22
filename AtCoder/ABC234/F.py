from collections import defaultdict

mod = 998244353
M = 5001

F = [1]
for i in range(1, M * 2):
  F.append(i * F[-1] % mod)

Finv = [None] * len(F)
Finv[-1] = pow(F[-1], mod - 2, mod)
for i in range(len(F) - 1, -1, -1):
  Finv[i - 1] = Finv[i] * i % mod


def comb(n, k):
  return F[n] * Finv[n - k] * Finv[k] % mod


S = input()

D = defaultdict(int)
for c in S:
  D[c] += 1

dp = [0] * M
dp[0] = 1

for c in D.values():
  dp_next = [0] * M

  for x in range(c + 1):
    for y, d in enumerate(dp):
      if d == 0: continue
      dp_next[x + y] += d * comb(x + y, y)
      dp_next[x + y] %= mod

  dp = dp_next

ans = (sum(dp) - 1) % mod
print(ans)
