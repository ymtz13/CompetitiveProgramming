from itertools import permutations

N, M, R = list(map(int, input().split()))
r = list(map(int, input().split()))
INF=10**30
D = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(M):
    A, B, C = list(map(int, input().split()))
    D[A][B] = D[B][A] = C

for k in range(1,N+1):
    for j in range(1,N+1):
        for i in range(j+1,N+1):
            D[i][j] = D[j][i] = min(D[i][j], D[i][k]+D[k][j])

for i in range(1,N+1):
    print(D[i][1:])

ans = INF
for path in permutations(r):
    length = 0
    for i in range(R-1):
        length += D[path[i]][path[i+1]]
    ans = min(ans, length)

print(ans)

    
