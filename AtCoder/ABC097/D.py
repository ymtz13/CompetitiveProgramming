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
P = list(map(int, input().split()))
L = [None]*N
for l, p in enumerate(P):
    L[p-1] = l
uf = UF(N)
for _ in range(M):
    x, y = list(map(int, input().split()))
    uf.union(x-1, y-1)

ans = 0
for i in range(N):
    if uf.find(i)==uf.find(L[i]): ans+=1

print(ans)
