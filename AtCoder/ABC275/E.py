mod = 998244353

N, M, K = map(int, input().split())

invM = pow(M, mod - 2, mod)

dp = [0] * (N + 1)
dp[0] = 1

for _ in range(K):
  dp_next = [0] * (N + 1)
  dp_next[-1] = dp[-1]

  for s in range(N):
    for m in range(1, M + 1):
      t = s + m
      if t > N: t = N - (t - N)

      dp_next[t] += dp[s] * invM
      dp_next[t] %= mod

  dp = dp_next

print(dp[-1])
