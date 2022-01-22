N = int(input())
M = 1000001
E = [[] for _ in range(M)]
for i in range(1, N + 1):
  a, b = map(int, input().split())
  E[a].append((i, b))

dp = [None] * M
dp[-1] = (0, None, None)

for x in range(M - 2, -1, -1):
  n0, p0, _ = dp[x] = dp[x + 1]
  for i, a in E[x]:
    n, p, _ = dp[a]
    if n + 1 > n0 or (n + 1 == n0 and i < p0):
      n0, p0, _ = dp[x] = (n + 1, i, a)

ans = []
i = 0
while dp[i][2] is not None:
  ans.append(dp[i][1])
  i = dp[i][2]

print(len(ans))
print(' '.join(map(str, ans)))
