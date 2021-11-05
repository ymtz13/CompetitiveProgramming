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

N = int(input())
E = sorted([tuple(map(int, input().split())) for _ in range(N-1)], key=lambda x: x[2])

uf = UF(N)
ans = 0
for u, v, w in E:
  u -= 1
  v -= 1
  ans += uf.size(u) * uf.size(v) * w
  uf.union(u, v)

print(ans)
