from collections import deque

T = int(input())
Ans = []

for _ in range(T):
  N, M = map(int, input().split())
  C = list(map(int, input().split()))
  E = [[] for _ in range(N)]
  for _ in range(M):
    u, v = map(int, input().split())
    E[u - 1].append(v - 1)
    E[v - 1].append(u - 1)

  if C[0] == C[-1]:
    Ans.append(-1)
    continue

  N2 = N * N

  dist = [-1] * N2
  queue = deque([N - 1])
  goal = (N - 1) * N
  while queue:
    q = queue.popleft()
    d = q // N2
    c = q % N2
    if dist[c] > -1: continue
    dist[c] = d

    x = c // N
    y = c % N

    d += 1
    for ex in E[x]:
      for ey in E[y]:
        if C[ex] == C[ey]: continue

        e = ex * N + ey
        if dist[e] > -1: continue
        queue.append(d * N2 + e)

  ans = dist[goal]
  Ans.append(ans)

for a in Ans:
  print(a)
