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
        
N, M = map(int, input().split())
A = list(map(int, input().split()))
uf = UF(N)
for _ in range(M):
    x, y = map(int, input().split())
    uf.union(x,y)

D = {}
for x, a in enumerate(A):
    c = uf.find(x)
    if c not in D: D[c]=[]
    D[c].append(a)

ans = 0
L = []
for d in D.values():
    d.sort()
    ans += d[0]
    L += d[1:]
    print(d[0])

print(L, ans)
L.sort()

P = len(D)-2

if len(D)==1:
    ans = 0
elif len(L)>=P:
    ans += sum(L[:len(D)-2])
else:
    ans = 'Impossible'

print(ans)
