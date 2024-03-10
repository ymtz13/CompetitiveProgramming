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


N, Q = map(int, input().split())
Queries = [tuple(map(int, input().split())) for _ in range(Q)]

N = N + 1
uf = UF(N * 2)

for w, x, y, z in Queries:
    if w == 1:
        if z % 2 == 0:
            uf.union(x, y)
            uf.union(x + N, y + N)
        else:
            uf.union(x, y + N)
            uf.union(x + N, y)
    else:
        print("YES" if uf.find(x) == uf.find(y) else "NO")
