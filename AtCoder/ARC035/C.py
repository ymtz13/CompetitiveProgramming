INF = 10**16
N, M = map(int, input().split())
D = [[INF] * N for _ in range(N)]
for i in range(N):
  D[i][i] = 0

for _ in range(M):
  A, B, C = map(int, input().split())
  D[A - 1][B - 1] = D[B - 1][A - 1] = C

for k in range(N):
  for i in range(N):
    for j in range(i + 1, N):
      D[i][j] = D[j][i] = min(D[i][j], D[i][k] + D[k][j])

K = int(input())
for k in range(K):
  S = 0
  X, Y, Z = map(int, input().split())
  for i in range(N):
    for j in range(i + 1, N):
      d1 = D[i][X - 1] + D[Y - 1][j] + Z
      d2 = D[i][Y - 1] + D[X - 1][j] + Z
      d = min(D[i][j], d1, d2)
      D[i][j] = D[j][i] = d
      S += d
  print(S)
