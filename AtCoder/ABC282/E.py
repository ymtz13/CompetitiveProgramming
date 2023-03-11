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
A = list(map(int, input().split()))

E = []
for i, x in enumerate(A):
  for j, y in enumerate(A[:i]):
    c = (pow(x, y, M) + pow(y, x, M)) % M
    E.append((-c, i, j))

E.sort()

uf = UF(N)
ans = 0

for c, i, j in E:
  if uf.find(i) != uf.find(j):
    ans -= c
    uf.union(i, j)

print(ans)
