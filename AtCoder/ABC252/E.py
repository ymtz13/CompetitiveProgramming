from heapq import heappush, heappop

N, M = map(int, input().split())
E = [[] for _ in range(N)]

for i in range(M):
  A, B, C = map(int, input().split())
  E[A - 1].append((B - 1, C, i + 1))
  E[B - 1].append((A - 1, C, i + 1))

queue = [(0, 0, -1)]
dist = [None] * N
ans = []

while queue:
  d, q, i = heappop(queue)
  if dist[q] is not None: continue
  dist[q] = d
  ans.append(i)

  for e, c, i in E[q]:
    if dist[e] is None: heappush(queue, (d + c, e, i))

print(' '.join(map(str, ans[1:])))
