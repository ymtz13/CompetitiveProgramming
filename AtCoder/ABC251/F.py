from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  u, v = map(int, input().split())
  E[u - 1].append(v - 1)
  E[v - 1].append(u - 1)


def T1(N, E):
  queue = deque([(0, None)])
  visited = [False] * N
  res = []

  while queue:
    q, p = queue.pop()

    if visited[q]: continue
    visited[q] = True
    if p is not None: res.append((p, q))

    for e in E[q]:
      queue.append((e, q))

  return res


def T2(N, E):
  queue = deque([(0, None)])
  visited = [False] * N
  res = []

  while queue:
    q, p = queue.popleft()

    if visited[q]: continue
    visited[q] = True
    if p is not None: res.append((p, q))

    for e in E[q]:
      queue.append((e, q))

  return res


for u, v in T1(N, E) + T2(N, E):
  print(u + 1, v + 1)
