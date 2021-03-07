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

N, M, S = map(int, input().split())
E = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)
E[S].append(0)

uf = UF(N+1)
ans = []    
for n in range(N, 0, -1):
    for e in E[n]:
        if e>n or e==0: uf.union(n, e)

    if uf.find(n)==uf.find(0): ans.append(n)
        
print('\n'.join(map(str, ans[::-1])))
