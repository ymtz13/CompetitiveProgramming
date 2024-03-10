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
A = set(map(int, input().split()))

for n in range(N):
    if 1 << n == N:
        break

B = [1 << i for i in range(n - 1, -1, -1)]
V = [None] * n
X = []

for a in range(1, N):
    if a in A:
        continue

    x = a
    for i, (b, v) in enumerate(zip(B, V)):
        if b & x:
            if v is None:
                V[i] = x
                X.append(a)
                break
            else:
                x ^= v

if len(X) < n:
    print(-1)
    exit()

uf = UF(N)
edges = []

for x in X:
    for i in range(N):
        j = i ^ x
        if uf.find(i) != uf.find(j):
            uf.union(i, j)
            edges.append((i, j))

for i, j in edges:
    print(i, j)
