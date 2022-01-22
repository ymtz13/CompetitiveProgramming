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


N, M, Q = map(int, input().split())
E = []
for _ in range(M):
  a, b, c = map(int, input().split())
  E.append((1, a - 1, b - 1, c, None))

for q in range(Q):
  a, b, c = map(int, input().split())
  E.append((2, a - 1, b - 1, c, q))

E.sort(key=lambda e: e[3])

uf = UF(N)
ans = [None] * Q

for t, a, b, c, q in E:
  if t == 1:
    if uf.find(a) != uf.find(b):
      uf.union(a, b)

  else:
    ans[q] = 'Yes' if uf.find(a) != uf.find(b) else 'No'

for a in ans:
  print(a)
