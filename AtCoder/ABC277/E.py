from collections import deque
from heapq import heappop, heappush

N, M, K = map(int, input().split())
N2 = N * 2
E = [[] for _ in range(N2)]

for _ in range(M):
  u, v, a = map(int, input().split())
  u -= 1
  v -= 1

  u0 = u * 2
  v0 = v * 2
  u1 = u * 2 + 1
  v1 = v * 2 + 1

  if a == 1:
    E[u0].append(v0)
    E[v0].append(u0)
  else:
    E[u1].append(v1)
    E[v1].append(u1)

S = list(map(int, input().split()))
for s in S:
  s -= 1
  s0 = s * 2
  s1 = s * 2 + 1
  E[s0].append(s1)
  E[s1].append(s0)

INF = 1 << 60
heap = [0]
dist = [INF] * N2

while heap:
  v = heappop(heap)
  d = v // N2
  q = v % N2

  if dist[q] != INF: continue
  dist[q] = d

  for e in E[q]:
    dd = d if e // 2 == q // 2 else d + 1
    heappush(heap, dd * N2 + e)

ans = min(dist[-2:])
print(ans if ans < INF else -1)
