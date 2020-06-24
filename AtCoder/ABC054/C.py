N, M = list(map(int, input().split()))
E = [[False]*N for _ in range(N)]
for m in range(M):
    a, b = list(map(int, input().split()))
    E[a-1][b-1] = E[b-1][a-1] = True

P = []
V = [False]*N
V[0] = True
p = [0] + [None]*(N-1)
def dfs(i):
    if i==N:
        P.append(p[:])
        return
        
    for v, visited in enumerate(V):
        if not visited:
            p[i] = v
            V[v] = True
            dfs(i+1)
            V[v] = False

dfs(1)

ans = 0
for p in P:
    ok = True
    for i in range(N-1):
        if not E[p[i]][p[i+1]]:
            ok = False
            break
    if ok: ans+=1
print(ans)
        
