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
P = list(map(int, input().split()))

L = [None] * (N + 1)
for i, p in enumerate(P):
  L[p] = i

uf = UF(N + 1)

ans = 0
mod = 998244353
X = (M - 1) * M // 2

for i in range(N):
  x = i + 1
  p = P[i]

  if uf.find(x) != uf.find(p):
    c = uf.n - 1
    if c >= 2:
      ans += X * pow(M, c - 2, mod)
      ans %= mod

  uf.union(x, p)

print(ans)
