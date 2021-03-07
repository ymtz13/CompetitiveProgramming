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
XYI = sorted([(*map(int, input().split()), i) for i in range(N)])

uf = UF(N)

pi = None
py = N+1
for x, y, i in XYI:
    if y>py: uf.union(i, pi)
    else:
        pi = i
        py = y

pi = None
py = 0
for x, y, i in reversed(XYI):
    if y<py: uf.union(i, pi)
    else:
        pi = i
        py = y

XYI = [(y, x, i) for x, y, i in XYI]
XYI.sort()

pi = None
py = N+1
for x, y, i in XYI:
    if y>py: uf.union(i, pi)
    else:
        pi = i
        py = y

pi = None
py = 0
for x, y, i in reversed(XYI):
    if y<py: uf.union(i, pi)
    else:
        pi = i
        py = y

for i in range(N):
    print(uf.size(i))
