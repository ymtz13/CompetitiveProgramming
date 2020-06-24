N, M = list(map(int, input().split()))
P = sorted([tuple(map(int, input().split())) for _ in range(M)])
Q = []

i = 1
ip = 0
M = [None]*(N+1)
M[1] = 0
while i<N:
    while ip<len(P) and P[ip][0]<=i:
        p = P[ip]
        Q.append((p[0], p[1], p[2]+M[p[0]]))
        ip+=1

    print(i, Q)

    # remove path which R<=i
    Q.sort(key=lambda x:-x[1])
    j = len(Q)-1
    while j>=0 and Q[j][1]<=i: j-=1
    Q = Q[:j+1]
    print(Q)
    
    if len(Q)==0:
        print(-1)
        exit()
        
    qmin = min(Q, key=lambda x:x[2])
    for r in range(i+1, qmin[1]+1):
        M[r] = qmin[2]

    i = qmin[1]

print(M)
print(M[N])
