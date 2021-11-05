INF = 10**10

N, M = map(int, input().split())

D = [[INF]*N for _ in range(N)]
for i in range(N): D[i][i] = 0

for _ in range(M):
  A, B, C = map(int, input().split())
  D[A-1][B-1] = C

ans = 0
for k in range(N):
  for s in range(N):
    for t in range(N):
      d = min(D[s][t], D[s][k] + D[k][t])
      D[s][t] = d
      ans += d if d < INF else 0

print(ans)
