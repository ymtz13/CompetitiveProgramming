import sys
input = sys.stdin.readline
        
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

D = sorted([(A[i][j], i, j) for i in range(N) for j in range(i+1,N)])

INF = 10**20
E = [[INF]*N for _ in range(N)]

ans = 0

for a, i, j in D:
    # find shortest path from i to j
    p = [None]*N
    d = [INF]*N
    d[i] = 0
    visited = set()
    
    while len(visited)<N:
        du, u = INF, 0
        for v in range(N):
            if v in visited: continue
            if d[v]<du: du, u = d[v], v
        visited.add(u)

        update = False
        for v, e in enumerate(E[u]):
            if e==INF: continue
            if d[v] > d[u]+e:
                update = True
                d[v] = d[u]+e
                p[v] = u
            
        if not update: break

    if d[j]>a:
        E[i][j] = E[j][i] = a
        ans += a
    elif d[j]<a:
        print(-1)
        exit()

print(ans)
