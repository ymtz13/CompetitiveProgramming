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
E = [tuple(map(int, input().split())) for _ in range(M)]

K = int(input())
X = {x - 1 for x in map(int, input().split())}

uf = UF(N)
for i, (u, v) in enumerate(E):
    if i not in X:
        uf.union(u - 1, v - 1)

C = [0] * N
for i, (u, v) in enumerate(E):
    if i in X:
        C[uf.find(u - 1)] += 1
        C[uf.find(v - 1)] += 1

odd = [c for c in C if c % 2]
print("Yes" if len(odd) <= 2 else "No")
