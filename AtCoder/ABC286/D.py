N, X = map(int, input().split())
C = [tuple(map(int, input().split())) for _ in range(N)]

dp = [False] * (X + 1)
dp[0] = True

for A, B in C:
  for _ in range(B):
    for f in range(X - A, -1, -1):
      if dp[f]: dp[f + A] = True

print('Yes' if dp[X] else 'No')
