N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [-(1 << 60)] * (M + 1)
dp[0] = 0

for a in A:
  for i in range(M, 0, -1):
    dp[i] = max(dp[i], dp[i - 1] + i * a)

print(dp[M])
