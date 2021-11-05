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

N = int(input())
A = list(map(int, input().split()))

uf = UF(200001)

for a, b in zip(A, A[::-1]):
  uf.union(a, b)

ans = 0
s = set()
for a in range(200001):
  root = uf.find(a)
  if root not in s: 
    s.add(root)
    ans += uf.size(a) - 1

print(ans)
