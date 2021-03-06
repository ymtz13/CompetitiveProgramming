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
B = list(map(int, input().split()))

uf = UF(N)

for _ in range(M):
    c, d = map(int, input().split())
    uf.union(c-1, d-1)

SA = [0]*N
SB = [0]*N

for i in range(N):
    SA[uf.find(i)] += A[i]
    SB[uf.find(i)] += B[i]

ans = 'Yes'
for sa, sb in zip(SA, SB):
    if sa!=sb: ans = 'No'

print(ans)


    
