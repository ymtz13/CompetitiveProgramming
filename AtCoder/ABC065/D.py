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

import sys
input = sys.stdin.readline

N = int(input())
P = [tuple(map(int, [i]+input().split())) for i in range(N)]

uf = UF(N)

Px = sorted(P, key=lambda p:p[1])
Py = sorted(P, key=lambda p:p[2])

E = []
for i in range(N-1):
    E.append((Px[i+1][1]-Px[i][1], Px[i][0], Px[i+1][0]))
    E.append((Py[i+1][2]-Py[i][2], Py[i][0], Py[i+1][0]))
E = sorted(E)

ans = 0
for c, p1, p2 in E:
    if uf.find(p1)!=uf.find(p2):
        ans += c
        uf.union(p1, p2)

print(ans)
