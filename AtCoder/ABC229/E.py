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
E = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A - 1].append(B - 1)
  E[B - 1].append(A - 1)

ans = [None] * N
uf = UF(N)

for i in range(N - 1, -1, -1):
  ans[i] = uf.n - (i + 1)

  for e in E[i]:
    if e > i: uf.union(i, e)

for a in ans:
  print(a)
