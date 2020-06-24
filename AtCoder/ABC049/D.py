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

N, K, L = list(map(int, input().split()))
uf1, uf2 = UF(N), UF(N)
for _ in range(K):
    p, q = list(map(int, input().split()))
    uf1.union(p-1, q-1)

for _ in range(L):
    r, s = list(map(int, input().split()))
    uf2.union(r-1, s-1)

keys = [(uf1.find(x), uf2.find(x)) for x in range(N)]
count = {}
for key in keys:
    if key in count: count[key]+=1
    else: count[key]=1

print(*[count[key] for key in keys])
