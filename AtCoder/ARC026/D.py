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

N2 = N * 2


def f(X):
    EE = []
    for A, B, C, T in E:
        z = T * X - C
        A -= 1
        B -= 1
        EE.append((z, A, B))

    EE.sort(reverse=True)
    s = 0

    uf = UF(N)

    for z, A, B in EE:
        if z > 0 or uf.find(A) != uf.find(B):
            uf.union(A, B)
            s += z

    return s >= 0


ng = -1
ok = 10**7

while ok - ng > 1e-5:
    tgt = (ok + ng) / 2
    if f(tgt):
        ok = tgt
    else:
        ng = tgt

print(ok)
