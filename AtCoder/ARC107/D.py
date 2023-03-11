N, K = map(int, input().split())
mod = 998244353

N2 = N * 2 + 10

dp = [0] * N2
dp[0] = 1

for n in range(1, N + 1):
  dp_next = [0] * N2
  for k in range(N2 - 1, 0, -1):
    v = 0 if k == 1 else dp[k - 2]
    if k <= n: v += dp_next[k * 2]
    dp_next[k] = v % mod

  dp = dp_next

print(dp[K * 2])
