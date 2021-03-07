N = int(input())
XYZ = [tuple(map(int, input().split())) for _ in range(N)]

C = [[0]*N for _ in range(N)]
for i, (x, y, z) in enumerate(XYZ):
    for j, (X, Y, Z) in enumerate(XYZ):
        C[i][j] = abs(X-x) + abs(Y-y) + max(Z-z, 0)

M = N-1
D = [None] * (2**M)*M

for c in range(N-1):
    D[(1<<c)*M+c] = C[N-1][c]

def dfs(S, c):
    if D[S*M+c]: return D[S*M+c]

    retval = 10**20
    S_c = S - (1<<c)
    for x in range(N-1):
        b = 1<<x
        if (S_c&b)==0: continue

        retval = min(retval, dfs(S_c, x) + C[x][c])
    D[S*M+c] = retval
    return retval
    

ans = 10**20
bit = 2**M-1
for c in range(N-1):
    ans = min(ans, dfs(bit, c) + C[c][N-1])

print(ans)
