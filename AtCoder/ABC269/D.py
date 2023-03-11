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
P = [tuple(map(int, input().split())) for _ in range(N)]

uf = UF(N)

for i, (x, y) in enumerate(P):
  for j, p2 in enumerate(P[i + 1:], i + 1):
    s = {
        (x - 1, y - 1),
        (x - 1, y),
        (x, y - 1),
        (x + 1, y + 1),
        (x, y + 1),
        (x + 1, y),
    }

    if p2 in s: uf.union(i, j)

print(uf.n)
