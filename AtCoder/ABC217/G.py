N, M = map(int, input().split())
mod = 998244353

dp = [0] * (N + 2)
dp[1] = 1

for n in range(2, N + 1):
  c = (n - 1) // M
  dp_next = [0] * (N + 2)
  for k in range(N + 1):
    dp_next[k] += dp[k] * max(k - c, 0)
    dp_next[k + 1] += dp[k]
  dp = [v % mod for v in dp_next]

for ans in dp[1:-1]:
  print(ans)