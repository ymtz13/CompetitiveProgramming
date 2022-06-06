N, X = map(int, input().split())
dp = [False] * 10200
dp[0] = True

for _ in range(N):
  a, b = map(int, input().split())
  dp_next = [False] * 10200
  for i, v in enumerate(dp[:10010]):
    if v:
      dp_next[i + a] = True
      dp_next[i + b] = True

  dp = dp_next

print('Yes' if dp[X] else 'No')
