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
uf = UF(H + W - 3)
for h in range(H):
  nh = 0 if h == 0 or h == H - 1 else h
  for w, c in enumerate(input()):
    nw = 0 if w == 0 or w == W - 1 else w + H - 2
    if c == '#': uf.union(nh, nw)

sH = {uf.find(0)}
for h in range(1, H - 1):
  sH.add(uf.find(h))

sW = {uf.find(0)}
for w in range(H - 1, H + W - 3):
  sW.add(uf.find(w))

print(min(len(sH), len(sW)) - 1)
