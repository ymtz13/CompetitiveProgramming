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


N, M = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(M)]

uf = UF(N)

ans = 0
for a, b, c in sorted(E, key=lambda x: x[2]):
  if c <= 0 or uf.find(a - 1) != uf.find(b - 1):
    uf.union(a - 1, b - 1)
  else:
    ans += c

print(ans)
