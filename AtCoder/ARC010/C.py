n, m, Y, Z = map(int, input().split())
M = 1 << m
INF = 1 << 60
D = {}
P = []
for _ in range(m):
  c, p = input().split()
  if c not in D:
    D[c] = len(D)
    P.append(int(p))

B = input()

dp = [[None] * m for _ in range(M)]
for b in B:
  dp_next = [row[:] for row in dp]

  b = D[b]
  k = 1 << b

  dp_next[k][b] = P[b]

  for i in range(M):
    for j in range(m):
      if dp[i][j] is None: continue

      x = dp[i][j] + P[b]
      if i and j == b: x += Y

      y = dp_next[i | k][b]
      dp_next[i | k][b] = max(y if y is not None else -INF, x)

  dp = dp_next

for i in range(m):
  if dp[M - 1][i] is not None:
    dp[M - 1][i] += Z

ans = 0
for i in range(M):
  for j in range(m):
    if dp[i][j] is not None:
      ans = max(ans, dp[i][j])

print(ans)
