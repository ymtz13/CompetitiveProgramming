N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[1] * (M + 1) for _ in range(N + 1)]
mod = 10**9 + 7

for ia, a in enumerate(A, 1):
  for ib, b in enumerate(B, 1):
    dp[ia][ib] = dp[ia - 1][ib] + dp[ia][ib - 1] - dp[ia - 1][ib - 1]
    if a == b: dp[ia][ib] += dp[ia - 1][ib - 1]
    dp[ia][ib] %= mod

print(dp[-1][-1])
