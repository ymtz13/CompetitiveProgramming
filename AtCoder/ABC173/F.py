N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    E[u-1].append(v-1)
    E[v-1].append(u-1)

par = [None]*N
q = [(0, -1)]
iq = 0
while iq<len(q):
    x, p = q[iq]
    iq += 1

    if par[x] is not None: continue

    par[x] = p
    for chd in E[x]:
        q.append((chd, x))

ans = 0
for x in range(N):
    p = par[x]
    Nl = N-1 - max(x,p)
    Nr = min(x,p)
    Nb = abs(p-x)-1
    N1 = Nl*(Nl+1)//2 + Nr*(Nr+1)//2 + Nb*(Nb+1)//2

    Nl = N-1 - x
    Nr = x
    N2 = Nl*(Nl+1)//2 + Nr*(Nr+1)//2
    
    N3 = N2 - N1 # myself only

    deg = len(E[x])

    if x==0:
        N1=0
        N3=N2
    #print(x, deg, N1, N2, N3,max(0, deg-2) * N1, max(0, deg-1) * N3)
    #ans += max(0, deg-2) * N1
    #ans += max(0, deg-1) * N3

    ans += (deg-2) * N1
    ans += (deg-1) * N3

print(ans+N*(N+1)//2)
    
