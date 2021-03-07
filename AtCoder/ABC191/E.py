from heapq import heappop, heappush

INF = 10**10

N, M = map(int, input().split())
E = [[] for _ in range(N)]
L = [INF]*N
for _ in range(M):
  A, B, C = map(int, input().split())
  if A==B:
    L[A-1] = min(L[A-1], C)
  else:
    E[A-1].append((B-1, C))

D = [[-1]*N for _ in range(N)]

for s in range(N):
  queue = [(0, s)]
  dist = [-1]*N
  while queue:
    d, q = heappop(queue)
    if dist[q]>=0: continue
    dist[q] = d

    for e, c in E[q]:
      if dist[e] < 0: heappush(queue, (d+c, e))
    
  D[s] = dist

for s in range(N):
  ans = L[s]
  for x in range(N):
    if s==x: continue
    df = D[s][x]
    db = D[x][s]
    if df >= 0 and db >= 0:
      ans = min(ans, df+db)
  
  print(ans if ans<INF else -1)
