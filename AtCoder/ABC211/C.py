C = 'chokudai'
S = input()
N = len(S)
mod = 10**9+7

dp = [[1]*(N+1)] + [[0]*(N+1) for _ in range(8)]

for i, c in enumerate(C, 1):
  for x in range(1, N+1):
    dp[i][x] = dp[i][x-1]
    if S[x-1]==c: dp[i][x] += dp[i-1][x]
    dp[i][x] %= mod

print(dp[-1][-1])
