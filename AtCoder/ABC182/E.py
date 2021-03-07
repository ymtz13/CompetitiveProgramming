H, W, N, M = map(int, input().split())
B  = [[0]*W for _ in range(H)]
Bt = [[0]*H for _ in range(W)]

for _ in range(N):
  h, w = map(int, input().split())
  B[h-1][w-1] = Bt[w-1][h-1] = 1

for _ in range(M):
  h, w = map(int, input().split())
  B[h-1][w-1] = Bt[w-1][h-1] = 2

L = [[False]*W for _ in range(H)]

ans = 0

for h in range(H):
  Brow = B[h]
  on = False
  for w in range(W):
    b = Brow[w]
    if b == 1: on = True
    if b == 2: on = False
    if on and not L[h][w]:
      ans += 1
      L[h][w] = True
  
  on = False
  for w in range(W-1, -1, -1):
    b = Brow[w]
    if b == 1: on = True
    if b == 2: on = False
    if on and not L[h][w]:
      ans += 1
      L[h][w] = True

for w in range(W):
  Bcol = Bt[w]
  on = False
  for h in range(H):
    b = Bcol[h]
    if b == 1: on = True
    if b == 2: on = False
    if on and not L[h][w]:
      ans += 1
      L[h][w] = True
  
  on = False
  for h in range(H-1, -1, -1):
    b = Bcol[h]
    if b == 1: on = True
    if b == 2: on = False
    if on and not L[h][w]:
      ans += 1

print(ans)
