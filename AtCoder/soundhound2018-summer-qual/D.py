from heapq import heappop, heappush

N, M, S, T = map(int, input().split())
Ea = [[] for _ in range(N)]
Eb = [[] for _ in range(N)]
for _ in range(M):
  u, v, a, b = map(int, input().split())
  Ea[u-1].append((v-1, a))
  Ea[v-1].append((u-1, a))
  Eb[u-1].append((v-1, b))
  Eb[v-1].append((u-1, b))

def dijkstra(E, s):
  dist = [None]*N
  queue = [(0, s)]
  while queue:
    d, q = heappop(queue)
    if dist[q] is not None: continue
    dist[q] = d

    for e, v in E[q]:
      if dist[e] is None: heappush(queue, (d+v, e))
  
  return dist

Da = dijkstra(Ea, S-1)
Db = dijkstra(Eb, T-1)

m = 10**20
ans = [None]*N
for i in range(N-1, -1, -1):
  m = min(m, Da[i] + Db[i])
  ans[i] = m

for a in ans:
  print(10**15-a)
