N = int(input())
S = [tuple(map(int, input().split())) for _ in range(N)]

INF = 1 << 60

dp = [-INF] * 5
dp[0] = 0

prevT = 0
for T, X, A in S:
  dT = T - prevT

  dp_next = []
  for i in range(5):
    dp_next.append(max(dp[max(0, i - dT):min(5, i + dT + 1)]))

  dp_next[X] += A
  prevT = T

  dp = dp_next

print(max(dp))
