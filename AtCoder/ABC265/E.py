mod = 998244353

N, M = map(int, input().split())
X1, Y1, X2, Y2, X3, Y3 = map(int, input().split())

XY = [tuple(map(int, input().split())) for _ in range(M)]
V = 1 << 40
S = {x * V + y for x, y in XY}

K = N + 1
K2 = K * K
dp = [0] * (K * K * K)
dp[0] = 1

ans = 0

for n1 in range(K):
  x1 = X1 * n1
  y1 = Y1 * n1

  for n2 in range(K - n1):
    x2 = x1 + X2 * n2
    y2 = y1 + Y2 * n2

    for n3 in range(K - n1 - n2):
      x3 = x2 + X3 * n3
      y3 = y2 + Y3 * n3
      if x3 * V + y3 in S: continue

      key = n1 * K2 + n2 * K + n3

      if n1: dp[key] += dp[key - K2]
      if n2: dp[key] += dp[key - K]
      if n3: dp[key] += dp[key - 1]
      dp[key] %= mod

      if n1 + n2 + n3 == N:
        ans += dp[key]
        ans %= mod

print(ans)
