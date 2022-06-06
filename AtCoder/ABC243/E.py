INF = 1 << 60

N, M = map(int, input().split())
D = [[INF] * N for _ in range(N)]
E = [[None] * N for _ in range(N)]

for i in range(M):
  A, B, C = map(int, input().split())
  D[A - 1][B - 1] = D[B - 1][A - 1] = C
  E[A - 1][B - 1] = E[B - 1][A - 1] = i

for k in range(N):
  for i in range(N):
    for j in range(N):
      if D[i][k] + D[k][j] <= D[i][j]:
        D[i][j] = D[i][k] + D[k][j]
        E[i][j] = None

S = set()
for i in range(N):
  for j in range(N):
    if E[i][j] is not None:
      S.add(E[i][j])

print(M - len(S))
