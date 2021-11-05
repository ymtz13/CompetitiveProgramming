from collections import deque

N, G, M = map(int, input().split())
E = [[0] * (N + 1) for _ in range(N + 1)]
F = [[0] * (N + 1) for _ in range(N + 1)]

P = list(map(int, input().split()))
for p in P:
  E[p][N] = 1

for _ in range(M):
  a, b = map(int, input().split())
  E[a][b] = E[b][a] = 1

while True:
  queue = deque([(0, -1)])
  come_from = [None]*(N+1)
  while queue:
    q, c = queue.popleft()
    if come_from[q] is not None: continue
    come_from[q] = c

    for e in range(N+1):
      if F[q][e] < E[q][e]: 
        queue.append((e, q))
  
  if come_from[N] is None: break

  p = N
  while come_from[p] != -1:
    c = come_from[p]
    F[c][p] += 1
    F[p][c] -= 1
    p = c

ans = 0
for p in P:
  ans += F[p][N]

print(ans)
