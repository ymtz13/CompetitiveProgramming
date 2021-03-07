X, Y = map(int, input().split())
Z = X + Y
N = int(input())

dp = [[0]*601 for _ in range(301)] # dp[n][c]  n個以下かつc枚以下で得られる嬉しさの最大値
for n in range(1, N+1):
  t, h = map(int, input().split())
  for i in range(n, 0, -1):
    d0 = dp[i-1]
    d1 = dp[i]
    for j in range(600, t-1, -1):
      d1[j] = max(d1[j], d0[j-t] + h)

ans = 0
for d in dp[:X+1]:
  ans = max(ans, d[X+Y])

print(ans)
