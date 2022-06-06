N, P = map(int, input().split())

dp = [[0] * (N + 10) for _ in range(N + 10)]
ds = [[0] * (N + 10) for _ in range(N + 10)]
dp[0][0] = ds[0][0] = 1

for x in range(1, N + 1):
  for t in range(N + 10):
    for d in (1, 2, 3, 4):
      xf = max(0, x - 10**d + 1)
      xt = x - 10**(d - 1)

      if xt < 0 or t - d - 1 < 0: break

      if xf == 0:
        dp[t][x] += ds[t - d - 1][xt] * 25 + ds[t - d - 1][0]

      else:
        dp[t][x] += (ds[t - d - 1][xt] - ds[t - d - 1][xf - 1]) * 25

      dp[t][x] %= P

    ds[t][x] = (ds[t][x - 1] + dp[t][x]) % P

ans = 0
for t in range(N):
  ans += dp[t][N]
  ans %= P

print(ans)
