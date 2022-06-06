mod = 998244353

N, M, K = map(int, input().split())
dp = [0] * (N * M + 1)
dp[0] = 1

for _ in range(N):
  dp_next = [0] * (N * M + 1)
  for n, v in enumerate(dp):
    if v == 0: continue
    for i in range(n + 1, n + M + 1):
      dp_next[i] += v
      dp_next[i] %= mod
  dp = dp_next

print(sum(dp[:K + 1]) % mod)
