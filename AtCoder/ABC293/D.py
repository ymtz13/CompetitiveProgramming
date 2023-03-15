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


N, M = map(int, input().split())
ABCD = [tuple(input().split()) for _ in range(M)]

uf = UF(N)

for a, b, c, d in ABCD:
    a = int(a)
    c = int(c)
    uf.union(a - 1, c - 1)

cnt = [0] * N
for a, b, c, d in ABCD:
    a = int(a)
    cnt[uf.find(a - 1)] += 1

loop = 0
for i in range(N):
    r = uf.find(i)
    if i != r:
        continue

    if uf.size(i) == cnt[i]:
        loop += 1

print(loop, uf.n - loop)
