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


N = int(input())
S1 = input()
S2 = input()

uf = UF(26)
used = [False]*26
fixed = [False]*26
for c1, c2 in zip(S1, S2):
    d1 = ord(c1)-ord('A')
    d2 = ord(c2)-ord('A')

    if d1>=0: used[d1] = True
    if d2>=0: used[d2] = True

    if d1>=0 and d2>=0:
        uf.union(d1, d2)
        continue
        
    elif d1>=0:
        fixed[d1] = True
        
    elif d2>=0:
        fixed[d2] = True
        
G = [[] for _ in range(26)]
F = [False]*26
for c in range(26):
    if not used[c]: continue
    G[uf.find(c)].append(c)
    if fixed[c]: F[uf.find(c)]=True

ans = 1
for f, g in zip(F, G):
    if len(g)>0 and not f: ans *= 10

d1 = ord(S1[0])-ord('A')
d2 = ord(S2[0])-ord('A')
if d1>=0 and not F[uf.find(d1)]: ans = ans*9//10
print(ans)
