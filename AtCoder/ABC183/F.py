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

N, Q = map(int, input().split())
C = [None] + [{c: 1} for c in map(int, input().split())]

uf = UF(N+1)

for _ in range(Q):
  t, a, b = map(int, input().split())
  if t==1:
    fa = uf.find(a)
    fb = uf.find(b)
    if fa==fb: continue
  
    ca = C[fa]
    cb = C[fb]
    uf.union(a, b)

    if len(ca)<len(cb): ca, cb = cb, ca
    for k, v in cb.items():
      if k not in ca: ca[k] = 0
      ca[k] += v
    C[uf.find(a)] = ca

    print(uf.uf)
    print(C)
    print()

  else:
    c = C[uf.find(a)]
    print(c[b] if b in c else 0)



