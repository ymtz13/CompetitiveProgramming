from heapq import heappush, heappop

N, M = map(int, input().split())
H = list(map(int, input().split()))

E = [[] for _ in range(N)]
for _ in range(M):
  U, V = map(int, input().split())
  E[U - 1].append(V - 1)
  E[V - 1].append(U - 1)

queue = [(0, 0)]
dist = [None] * N
while queue:
  d, q = heappop(queue)
  if dist[q] is not None: continue
  dist[q] = d

  hq = H[q]
  for e in E[q]:
    he = H[e]
    cost = max(0, he - hq)
    heappush(queue, (d + cost, e))

ans = 0
h0 = H[0]
for h, d in zip(H, dist):
  ans = max(ans, h0 - h - d)

print(ans)
