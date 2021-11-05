from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A - 1].append(B - 1)
  E[B - 1].append(A - 1)

D = [None] * N
bipartite = True
n0 = n1 = 0
queue = deque([(0, 0)])
while queue:
  q, d = queue.popleft()

  if D[q] is not None:
    if D[q] != d: bipartite = False
    continue

  D[q] = d
  if d == 0: n0 += 1
  if d == 1: n1 += 1

  for e in E[q]:
    queue.append((e, 1 - d))

if bipartite:
  print(n0 * n1 - M)
else:
  print(N * (N - 1) // 2 - M)
