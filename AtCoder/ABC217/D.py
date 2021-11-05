from bisect import bisect

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


L, Q = map(int, input().split())
CX = [(i, ) + tuple(map(int, input().split())) for i in range(Q)]

X = []
for i, c, x in CX:
  if c == 1:
    X.append((i, x))

#print(X)

st = 0
sectors = []
lengths = []
merge_index = {}
for i, x in sorted(X, key=lambda x: x[1]):
  sectors.append((st, x))
  lengths.append(x - st)
  st = x
  merge_index[i] = len(sectors) - 1

sectors.append((st, L))
lengths.append(L - st)

#print(sectors)
#print(lengths)
#print(merge_index)

uf = UF(len(sectors))
ans = []
for i, c, x in reversed(CX):
  if c == 1:
    idx = merge_index[i]
    lenL = lengths[uf.find(idx)]
    lenR = lengths[uf.find(idx + 1)]
    uf.union(idx, idx + 1)
    lengths[uf.find(idx)] = lenL + lenR
  
  if c==2:
    idx = bisect(sectors, (x, x)) - 1
    ans.append(lengths[uf.find(idx)])

for a in ans[::-1]:
  print(a)
