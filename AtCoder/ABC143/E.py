from collections import deque

N, M, L = map(int, input().split())
D = [[L + 1] * N for _ in range(N)]
for i in range(N):
  D[i][i] = 0

for _ in range(M):
  A, B, C = map(int, input().split())
  D[A - 1][B - 1] = D[B - 1][A - 1] = min(L + 1, C)

for k in range(N):
  for i in range(N):
    for j in range(N):
      D[i][j] = D[j][i] = min(D[i][j], D[i][k] + D[k][j])

E = [[] for _ in range(N)]
for i in range(N):
  for j in range(N):
    if D[i][j] <= L:
      E[i].append(j)
      E[j].append(i)

dists = []
for s in range(N):
  queue = deque([(s, -1)])
  dist = [N + 1] * N
  while queue:
    q, d = queue.popleft()
    if dist[q] <= d: continue
    dist[q] = d

    for e in E[q]:
      queue.append((e, d + 1))

  dists.append(dist)

Q = int(input())
for _ in range(Q):
  s, t = map(int, input().split())
  ans = dists[s - 1][t - 1]
  print(ans if ans < N + 1 else -1)
