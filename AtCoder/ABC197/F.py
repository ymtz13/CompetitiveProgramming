from heapq import heappop, heappush

N, M = map(int, input().split())
oa = ord('a')

E = [[False]*N for _ in range(N)]
EZ = [[set() for _ in range(26)] for _ in range(N)] # EZ[v][ord(c)] : vからcを介して到達できる点
for _ in range(M):
  A, B, C = input().split()
  A = int(A)
  B = int(B)
  E[A-1][B-1] = E[B-1][A-1] = True
  EZ[A-1][ord(C)-oa].add(B-1)
  EZ[B-1][ord(C)-oa].add(A-1)

INF = 10**10
D = [[INF]*N for _ in range(N)]


queue = [(0, 0, N-1)]
while queue:
  d, v1, v2 = heappop(queue)
  if D[v1][v2] < d: continue
  D[v1][v2] = D[v2][v1] = d

  for c in range(26):
    s1 = EZ[v1][c]
    s2 = EZ[v2][c]

    for w1 in s1:
      for w2 in s2:
        if D[w1][w2]==INF:
          heappush(queue, (d+1, w1, w2))
          D[w1][w2] = D[w2][w1] = d+1
  

ans = INF
for v1 in range(N):
  if D[v1][v1] < INF: ans = min(ans, D[v1][v1]*2)
  for v2 in range(v1+1, N):
    if D[v1][v2] < INF and E[v1][v2]:
      ans = min(ans, D[v1][v2]*2+1)

print(ans if ans<INF else -1)
