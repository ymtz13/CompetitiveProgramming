N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

parent = [None]*N
depth = [0]*N
d = 0
queue = [0]
while queue:
    d += 1
    queue_new = []
    for q in queue:
        for e in E[q]:
            if e==parent[q]: continue
            parent[e] = q
            depth[e] = d
            queue_new.append(e)
    queue = queue_new

ancestor = [[None]*N for _ in range(N)]
for a in range(N):
    for b in range(a, N):
        _a = a
        _b = b
        while _a!=_b:
            if depth[_a] < depth[_b]: _b = parent[_b]
            else: _a = parent[_a]
        ancestor[a][b] = ancestor[b][a] = _a

M = int(input())
P = []
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    w = ancestor[u][v]
    path = set()
    while u!=w:
        _u = parent[u]
        #path.add((u, _u))
        path.add(u*N+_u)
        u = _u
    while v!=w:
        _v = parent[v]
        #path.add((v, _v))
        path.add(v*N+_v)
        v = _v
    P.append(path)


ans = 0
n1 = N-1
for k in range(2**M):
    path = set()
    n = 0
    for i, p in enumerate(P):
        if (k>>i)&1:
            path |= p
            n += 1

    if n==0: continue
    sign = +1 if n&1 else -1
    ans += sign * pow(2, n1-len(path))
    
print(pow(2, N-1) - ans)
