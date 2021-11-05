from collections import deque

N, M = map(int, input().split())
ST = []
E = [[] for _ in range(N)]

for i in range(M):
  s, t = map(int, input().split())
  ST.append((i, s, t))
  E[s - 1].append((t - 1, i))

queue = deque([(0, 0, None, None)])
dist = [-1] * N
come_from = [None] * N
while queue:
  q, d, node_from, edge = queue.popleft()
  if dist[q] >= 0: continue
  dist[q] = d
  come_from[q] = (node_from, edge)

  for t, i in E[q]:
    queue.append((t, d + 1, q, i))

used_edges = set()
d0 = dist[-1]

if d0 >= 0:
  q = N - 1
  while q != 0:
    q, edge = come_from[q]
    used_edges.add(edge)


def getDist(blocked):
  queue = deque([(0, 0)])
  dist = [-1] * N
  while queue:
    q, d = queue.popleft()
    if dist[q] >= 0: continue
    dist[q] = d

    for t, i in E[q]:
      if i == blocked: continue
      queue.append((t, d + 1))

  return dist[-1]


for i in range(M):
  if i in used_edges:
    print(getDist(i))
  else:
    print(d0)
