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

uf = UF(N)

for _ in range(M):
    u, v = map(int, input().split())
    uf.union(u - 1, v - 1)

K = int(input())
C = set()
for _ in range(K):
    x, y = map(int, input().split())
    rx = uf.find(x - 1)
    ry = uf.find(y - 1)

    xy = tuple(sorted([rx, ry]))
    C.add(xy)

Q = int(input())
ans = []
for _ in range(Q):
    p, q = map(int, input().split())
    rp = uf.find(p - 1)
    rq = uf.find(q - 1)

    pq = tuple(sorted([rp, rq]))
    ans.append("No" if pq in C else "Yes")


for a in ans:
    print(a)
