class UF:
  def __init__(self, N):
    self.uf = [-1] * N
    self.n = N

  def find(self, x):
    if self.uf[x] < 0: return x
    self.uf[x] = self.find(self.uf[x])
    return self.uf[x]

  def size(self, x):
    return -self.uf[self.find(x)]

  def union(self, x, y):
    x, y = self.find(x), self.find(y)
    if x == y: return
    if self.size(x) > self.size(y): x, y = y, x
    self.uf[y] += self.uf[x]
    self.uf[x] = y
    self.n -= 1

H, W = map(int, input().split())
uf = UF((H+2)*(W+2))
M = [[False]*(W+2) for _ in range(H+2)]

Q = int(input())
for _ in range(Q):
  q = tuple(map(int, input().split()))
  if q[0]==1:
    _, r, c = q
    M[r][c] = True
    x = r*W+c
    if M[r-1][c  ]: uf.union(x, x-W)
    if M[r+1][c  ]: uf.union(x, x+W)
    if M[r  ][c-1]: uf.union(x, x-1)
    if M[r  ][c+1]: uf.union(x, x+1)
  
  else:
    _, r1, c1, r2, c2 = q
    print('Yes' if M[r1][c1] and uf.find(r1*W+c1) == uf.find(r2*W+c2) else 'No')
