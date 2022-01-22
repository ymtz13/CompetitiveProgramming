N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = 1 << 60
dp = [INF] * (1 << N)
dp[0] = 0

for used in range(1 << N):
  cnt = 0
  for i in range(N):
    b = 1 << i
    if used & b: cnt += 1

  not_used = 0
  for i in range(N):
    b = 1 << i
    if used & b == 0:
      cost = not_used * Y + abs(B[i] - A[cnt]) * X
      dp[used + b] = min(dp[used + b], dp[used] + cost)

      not_used += 1

print(dp[-1])
