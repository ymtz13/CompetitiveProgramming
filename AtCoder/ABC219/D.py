N = int(input())
X, Y = map(int, input().split())

dp = [[N + 1] * (Y + 1) for _ in range(X + 1)]
dp[0][0] = 0

for _ in range(N):
  A, B = map(int, input().split())

  dp_next = [row[:] for row in dp]
  for x in range(X + 1):
    for y in range(Y + 1):
      if dp[x][y] > N: continue

      tx = min(x + A, X)
      ty = min(y + B, Y)
      dp_next[tx][ty] = min(dp_next[tx][ty], dp[x][y] + 1)

  dp = dp_next

ans = dp[X][Y]
print(ans if ans <= N else -1)
