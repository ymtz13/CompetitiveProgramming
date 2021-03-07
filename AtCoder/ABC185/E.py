N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[N+M]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, M+1):
    a = A[i-1]
    b = B[j-1]
    if a==b:
      dp[i][j] = dp[i-1][j-1] - 2
    else:
      dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] - 1)

print(dp[N][M])