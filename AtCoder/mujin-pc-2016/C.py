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
E = []
for _ in range(M):
  x, y = map(int, input().split())
  E.append((x - 1, y - 1))

ans = 0
for B in range(1 << (N-1)):
  T = [None] * N
  for i in range(N):
    T[i] = (B >> i) & 1
  
  uf = UF(N)

  for x, y in E:
    if T[x] != T[y]: uf.union(x, y)

  ok = True
  for x, y in E:
    if T[x] == T[y] and uf.find(x) != uf.find(y):
      ok = False
      break
  
  if ok: ans += 1

print(ans)

