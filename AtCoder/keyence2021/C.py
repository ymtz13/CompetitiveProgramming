H, W, K = map(int, input().split())
C = [['_']*(W+1) for _ in range(H+1)]
for _ in range(K):
  h, w, c = input().split()
  C[int(h)-1][int(w)-1] = c

X = [0]*(W+1)
X[W-1] = 3 if C[H-1][W-1] == '_' else 1
C[H-1][W-1] = 'D'

mod = 998244353

cB = [0]*W
Z = [1]
p = 1
for _ in range(5001):
  p = p*3%mod
  Z.append(p)

for h in range(H-1, -1, -1):
  nX = [0]*(W+1)
  rB = 0
  for w in range(W-1, -1, -1):
    c = C[h][w]
    XR = nX[w+1] * Z[cB[w]] % mod
    XD = X[w] * Z[rB] % mod
    if c == 'R': v = XR % mod
    if c == 'D': v = XD % mod
    if c == 'X': v = (XR + XD) % mod
    if c == '_': v = (XR + XD) * 2 % mod
    nX[w] = v

    if c == '_':
      cB[w] += 1
      rB += 1
    
  X = nX
    
print(X[0])
