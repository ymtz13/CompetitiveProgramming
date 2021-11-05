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


M = 300000
uf = UF(M)
offset = M // 2

N = int(input())
C = [0] * M
for _ in range(N):
  x, y = map(int, input().split())
  C[x] += 1
  uf.union(x, offset + y)

S = [[] for _ in range(M)]
for i in range(M):
  S[uf.find(i)].append(i)

ans = 0

for s in S:
  x = [i for i in s if i < offset]
  y = [i - offset for i in s if i > offset]
  if len(x) < 2 or len(y) < 2: continue

  p = len(x) * len(y)
  q = sum([C[i] for i in x])
  ans += p - q

print(ans)
