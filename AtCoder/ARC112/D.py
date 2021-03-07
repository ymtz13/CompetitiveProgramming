class UF:
  def __init__(self, N):
    self.uf = [-1]*N
    self.n = N

  def find(self, x):
    if self.uf[x]<0: return x
    self.uf[x] = self.find(self.uf[x])
    return self.uf[x]

  def size(self, x):
    return -self.uf[self.find(x)]

  def union(self, x, y):
    x, y = self.find(x), self.find(y)
    if x==y: return
    if self.size(x) > self.size(y): x, y = y, x
    self.uf[y] += self.uf[x]
    self.uf[x] = y
    self.n -= 1

H, W = map(int, input().split())
uf = UF(H+W+1)
for h in range(H):
  nh = 0 if h==0 or h==H-1 else h+1
  for w, c in enumerate(input()):
    nw = 0 if w==0 or w==W-1 else w+H
    if nh!=nw:
      uf.union(nh, nw)

print(uf.n-1)
