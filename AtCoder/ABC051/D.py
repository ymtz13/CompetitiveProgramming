N, M = list(map(int, input().split()))
INF = 10**9
D = [[INF ]*N for _ in range(N)]
P = [[None]*N for _ in range(N)]
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    if a>b: a,b = b,a
    D[a-1][b-1] = D[b-1][a-1] = c
    P[a-1][b-1] = P[b-1][a-1] = (a-1)*N+b-1

for k in range(N):
    for i in range(N):
        for j in range(i+1, N):
            Dikj = D[i][k] + D[k][j]
            if D[i][j] > Dikj:
                D[i][j] = D[j][i] = Dikj
                P[i][j] = P[j][i] = (P[i][k], P[k][j])

E = set()
for i in range(N):
    for j in range(i+1, N):
        queue = [P[i][j]]
        while queue:
            queue_new = []
            for q in queue:
                if type(q) is tuple:
                    for x in q:
                        queue_new.append(x)
                else:
                    E.add(q)
            queue = queue_new

#ans = 0
#for i in range(N):
#    for j in range(i+1,N):
#        print(i, j, D[i][j])
#        if D[i][j] < INF: ans +=1
print(M-len(E))
