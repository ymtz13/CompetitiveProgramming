N = int(input())
M = 1010
X = [[0]*M for _ in range(M)]

for _ in range(N):
  lx, ly, rx, ry = map(int, input().split())
  X[lx][ly] += 1
  X[rx][ry] += 1
  X[lx][ry] -= 1
  X[rx][ly] -= 1

Y = [[0]*M for _ in range(M)]
for iy in range(M):
  s = 0
  for ix in range(M):
    s += X[ix][iy]
    Y[ix][iy] = s

A = [[0]*M for _ in range(M)]
for ix in range(M):
  s = 0
  for iy in range(M):
    s += Y[ix][iy]
    A[ix][iy] = s

ans = [0]*(N+1)
for row in A:
  for a in row:
    ans[a] += 1

for a in ans[1:]:
  print(a)
