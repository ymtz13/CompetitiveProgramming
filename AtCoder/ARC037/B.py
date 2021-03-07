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

N, M = map(int, input().split())
uf = UF(N)
loop = [False]*N

for _ in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  fu = uf.find(u)
  fv = uf.find(v)
  if fu==fv:
    loop[u] = loop[v] = True
  else:
    uf.union(u, v)

for i in range(N):
  if loop[i]: loop[uf.find(i)] = True

T = [0]*N
for i in range(N):
  fi = uf.find(i)
  if not loop[fi]: T[fi] = 1

print(sum(T))
