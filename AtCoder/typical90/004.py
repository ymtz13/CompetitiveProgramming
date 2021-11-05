H, W = map(int, input().split())
SX = []
SY = [0]*W
M = []
for _ in range(H):
  A = list(map(int, input().split()))
  M.append(A)
  SX.append(sum(A))
  for w, a in enumerate(A):
    SY[w] += a

for h, A in enumerate(M):
  ans = []
  for w, s in enumerate(SY):
    ans.append(s + SX[h] - A[w])
  print(' '.join(map(str, ans))) 
