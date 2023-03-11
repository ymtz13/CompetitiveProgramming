N, K, D = map(int, input().split())
A = list(map(int, input().split()))

INF = 1 << 60
dp = [[-INF] * D for _ in range(K + 1)]
dp[0][0] = 0

for a in A:
  for k in range(K - 1, -1, -1):
    for i in range(D):
      j = (i + a) % D
      dp[k + 1][j] = max(dp[k + 1][j], dp[k][i] + a)

ans = dp[K][0]
print(ans if ans >= 0 else -1)
