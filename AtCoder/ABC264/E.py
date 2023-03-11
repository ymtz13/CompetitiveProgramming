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


N, M, E = map(int, input().split())
W = [tuple(map(int, input().split())) for _ in range(E)]
Q = int(input())
X = [int(input()) for _ in range(Q)]

SX = set(X)
W0 = [w for i, w in enumerate(W, 1) if i not in SX]
WX = [W[x - 1] for x in X[::-1]]

uf = UF(N + M)
C = [1] * N + [0] * M
T = [0] * N + [1] * M

Ans = [0]
ans = 0

for w in W0 + WX:
  u, v = w
  u -= 1
  v -= 1

  ru = uf.find(u)
  rv = uf.find(v)

  if ru == rv:
    Ans.append(ans)
    continue

  cu = C[ru]
  cv = C[rv]
  tu = T[ru]
  tv = T[rv]
  uf.union(u, v)
  r = uf.find(u)

  C[r] = cu + cv
  T[r] = max(tu, tv)

  if tu == 1 and tv == 0:
    ans += cv
  if tu == 0 and tv == 1:
    ans += cu

  Ans.append(ans)

for a in Ans[len(W0):-1][::-1]:
  print(a)
