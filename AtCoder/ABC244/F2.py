from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  u, v = map(int, input().split())
  E[u - 1].append(v - 1)
  E[v - 1].append(u - 1)

B = [1 << i for i in range(N)]

X = 1 << N

dp = [None] * (X * N)
for i in range(N):
  dp[i] = 0

queue = deque([(b * N + i, 1) for i, b in enumerate(B)])
while queue:
  x, d = queue.popleft()
  if dp[x] is not None: continue
  dp[x] = d

  b, i = x // N, x % N

  for e in E[i]:
    queue.append(((b ^ B[e]) * N + e, d + 1))

ans = 0
for b in range(1 << N):
  ans += min(dp[b * N:b * N + N])

print(ans)
