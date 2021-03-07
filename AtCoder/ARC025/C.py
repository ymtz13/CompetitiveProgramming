import heapq

N, M, R, T = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  a, b, c = map(int, input().split())
  E[a-1].append((b-1, c))
  E[b-1].append((a-1, c))

ans = 0
for A in range(N):
  queue = [(0, A)]
  dist = [-1]*N
  while queue:
    d, q = heapq.heappop(queue)
    if dist[q] >= 0: continue
    dist[q] = d

    for e, c in E[q]:
      if dist[e] < 0: heapq.heappush(queue, (d+c, e))
  
  dist = sorted(dist)[1:]

  iT = -1
  for iR, dR in enumerate(dist):
    # dR/R > dT/T => dR*T > dT*R
    while iT < N-2 and dist[iT+1]*R < dR*T: iT += 1
    ans += iT + 1 if iT < iR else iT

print(ans)
    