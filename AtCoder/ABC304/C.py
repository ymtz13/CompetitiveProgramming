class UF:
    def __init__(self, N):
        self.uf = [-1] * N
        self.n = N

    def find(self, x):
        if self.uf[x] < 0:
            return x
        self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def size(self, x):
        return -self.uf[self.find(x)]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size(x) > self.size(y):
            x, y = y, x
        self.uf[y] += self.uf[x]
        self.uf[x] = y
        self.n -= 1


N, D = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(N)]

uf = UF(N)

D2 = D * D

for i1, (x1, y1) in enumerate(XY):
    for i2, (x2, y2) in enumerate(XY[i1 + 1 :], i1 + 1):
        dx = x1 - x2
        dy = y1 - y2
        d2 = dx * dx + dy * dy

        if d2 <= D2:
            uf.union(i1, i2)

for i in range(N):
    if uf.find(0) == uf.find(i):
        print("Yes")
    else:
        print("No")
