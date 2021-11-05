mod = 998244353
M = 3000
N, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [0] * (M + 1)

ans = 0
for n, a in enumerate(A, 1):
  for x in range(M, a, -1):
    dp[x] += dp[x - a]
    dp[x] %= mod
  dp[a] += n
  dp[a] %= mod
  ans += dp[S]
  ans %= mod

print(ans)
