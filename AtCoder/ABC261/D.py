N, M = map(int, input().split())
X = list(map(int, input().split()))
B = [0] * (N + 1)

for _ in range(M):
  C, Y = map(int, input().split())
  B[C] = Y

INF = 1 << 60
dp = [-INF] * (N + 1)
dp[0] = 0

for x in X:
  dp_next = [max(dp)] + [v + x for v in dp[:-1]]

  for i, b in enumerate(B):
    dp_next[i] += b

  dp = dp_next

print(max(dp))
