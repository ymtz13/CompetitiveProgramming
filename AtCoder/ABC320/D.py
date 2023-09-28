from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N + 1)]

for _ in range(M):
  A, B, X, Y = map(int, input().split())
  E[A].append((B, X, Y))
  E[B].append((A, -X, -Y))

ansX = [None] * (N + 1)
ansY = [None] * (N + 1)

queue = deque([(1, 0, 0)])
while queue:
  q, x, y = queue.popleft()
  if ansX[q] is not None: continue
  ansX[q] = x
  ansY[q] = y

  for e, dx, dy in E[q]:
    queue.append((e, x + dx, y + dy))

for i in range(1, N + 1):
  if ansX[i] is not None:
    print(ansX[i], ansY[i])
  else:
    print('undecidable')
