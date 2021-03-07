N = int(input())
D = [tuple(map(int, input().split())) for _ in range(N)]
S = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
  s = 0
  for j in range(N):
    s += D[i][j]
    S[i+1][j+1] = S[i][j+1] + s

M = [0]*2501

for i in range(N):
  for j in range(N):
    for x in range(i+1, N+1):
      for y in range(j+1, N+1):
        s = (x-i)*(y-j)
        M[s] = max(M[s], S[x][y] - S[i][y] - S[x][j] + S[i][j])

for i in range(1, 2501):
  M[i] = max(M[i-1], M[i])

Q = int(input())
for q in range(Q):
  P = int(input())
  print(M[P])
