H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
mod = 998244353

DH = H - 2 if x1 != x2 else H - 1
DW = W - 2 if y1 != y2 else W - 1

dp = [[0] * 3 for _ in range(3)]
dp[0][0] = 1

for _ in range(K):
  dp_next = [[0] * 3 for _ in range(3)]

  for fx, fy in ((0, 0), (0, 1), (1, 0), (1, 1)):
    dp_next[1 - fx][fy] += dp[fx][fy]
    dp_next[fx][1 - fy] += dp[fx][fy]
    dp_next[2][fy] += dp[fx][fy] * DH
    dp_next[fx][2] += dp[fx][fy] * DW

    dp_next[fx][fy] += dp[2][fy]
    dp_next[fx][fy] += dp[fx][2]

  dp_next[2][0] += dp[2][0] * (DH - 1)
  dp_next[2][1] += dp[2][1] * (DH - 1)
  dp_next[0][2] += dp[0][2] * (DW - 1)
  dp_next[1][2] += dp[1][2] * (DW - 1)
  dp_next[2][2] += dp[2][2] * (DH + DW - 2)

  for f in range(2):
    dp_next[2][1 - f] += dp[2][f]
    dp_next[2][2] += dp[2][f] * DW
    dp_next[2][f] += dp[2][2]

    dp_next[1 - f][2] += dp[f][2]
    dp_next[2][2] += dp[f][2] * DH
    dp_next[f][2] += dp[2][2]

  if x1 == x2:
    dp_next[1][0] = dp_next[1][1] = dp_next[1][2] = 0
  if y1 == y2:
    dp_next[0][1] = dp_next[1][1] = dp_next[2][1] = 0

  print(_, dp_next)
  for x in range(3):
    for y in range(3):
      dp_next[x][y] %= mod

  dp = dp_next

x = 1 if x1 != x2 else 0
y = 1 if y1 != y2 else 0
print(dp[x][y])
