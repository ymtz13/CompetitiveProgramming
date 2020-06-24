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

N, M, K = map(int, input().split())
uf = UF(N)

F = [0]*N # number of friends
for _ in range(M):
    A, B = map(int, input().split())
    uf.union(A-1, B-1)
    F[A-1] += 1
    F[B-1] += 1

G = [0]*N # number of candidates
for i in range(N):
    G[i] = uf.size(i) - F[i] - 1

for _ in range(K):
    C, D = map(int, input().split())
    if uf.find(C-1)!=uf.find(D-1): continue

    G[C-1] -= 1
    G[D-1] -= 1

print(*G)

    
