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

N, K = map(int, input().split())
R = [tuple(map(int, input().split())) for _ in range(N)]
C = [tuple([R[r][c] for r in range(N)]) for c in range(N)]
mod = 998244353

ufR = UF(N)
ufC = UF(N)

def swappable(v1, v2):
    ok = True
    for x1, x2 in zip(v1, v2):
        ok = ok and x1+x2<=K
    return ok
    
for i in range(N):
    for j in range(i+1, N):
        if swappable(R[i], R[j]): ufR.union(i, j)
        if swappable(C[i], C[j]): ufC.union(i, j)

f = [1]
for p in range(1, 60):
    f.append(f[-1]*p%mod)

ans = 1
for size in ufR.uf:
    if size>=0: continue
    ans = ans * f[-size] % mod
    
for size in ufC.uf:
    if size>=0: continue
    ans = ans * f[-size] % mod

print(ans)