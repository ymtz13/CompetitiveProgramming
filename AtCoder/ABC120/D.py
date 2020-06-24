N, M = list(map(int, input().split()))
AB = [tuple(map(int, input().split())) for _ in range(M)]

uf = [-1]*N

def find(x):
    if uf[x]<0: return x
    uf[x] = find(uf[x])
    return uf[x]        

def size(x):
    return -uf[find(x)]

def union(x, y):
    x, y = find(x), find(y)
    if size(x) > size(y): x, y = y, x
    uf[y] += uf[x]
    uf[x] = y

c = [N*(N-1)//2]
for a, b in reversed(AB):
    if find(a-1) != find(b-1):
        sa, sb = size(a-1), size(b-1)
        union(a-1, b-1)
        c.append(c[-1]-sa*sb)
    else:
        c.append(c[-1])

for t in reversed(c[:-1]):
    print(t)
