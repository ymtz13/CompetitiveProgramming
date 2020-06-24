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
E = [tuple(map(int, input().split())) for _ in range(M)]

ans = 0
for i in range(M):
    uf = UF(N)
    for j in range(M):
        if i==j: continue
        a, b = E[j]
        uf.union(a-1, b-1)
    if uf.n==2: ans+=1

print(ans)
        
