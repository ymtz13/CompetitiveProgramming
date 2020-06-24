N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    CA = list(map(int, input().split()))
    C.append(CA[0])
    A.append(CA[1:])

INF = 10**10
ans = INF
for x in range(1<<N):
    cost=0
    R=[0]*M
    for i in range(N):
        if (x>>i)&1: continue
        cost+=C[i]
        for m,a in enumerate(A[i]):
            R[m]+=a

    if min(R)>=X:
        ans=min(ans,cost)

print(-1 if ans==INF else ans)
