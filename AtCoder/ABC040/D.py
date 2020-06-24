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

N, M = list(map(int, input().split()))
E = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x:-x[2]) + [(0,0,-1)]
Q = int(input())
X = sorted([list(map(int, input().split())) + [iq, None] for iq in range(Q)], key=lambda x:-x[1])

uf = UF(N)

ie = 0
e = E[0]
for iq in range(Q):
    x = X[iq]
    while e[2]>x[1]:
        uf.union(e[0]-1, e[1]-1)
        ie += 1
        e = E[ie]

    x[3] = uf.size(x[0]-1)

X = sorted(X, key=lambda x:x[2])
for x in X:
    print(x[3])


