N, K = map(int, input().split())
S = input()

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1

mod = 10**9 + 7

for n, c in enumerate(S, 1):
  for n0 in range(n + 1):
    n1 = n - n0
    if abs(n1 - n0) > K: continue

    if c != '1' and n0 > 0: dp[n0][n1] += dp[n0 - 1][n1]
    if c != '0' and n1 > 0: dp[n0][n1] += dp[n0][n1 - 1]
    dp[n0][n1] %= mod

for d in dp:
  print(dp)

ans = 0
for n0 in range(N + 1):
  n1 = N - n0
  ans += dp[n0][n1]

print(ans)
