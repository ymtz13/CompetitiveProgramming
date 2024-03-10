N, M, Q = map(int, input().split())

S = [[0] * (M + 2)]
S.extend([[0] + list(map(int, input())) + [0] for _ in range(N)])
S.append([0] * (M + 2))

U = [[[0] * (M + 2) for _ in range(N + 2)] for _ in range(4)]
V = [[0] * (M + 2) for _ in range(N + 2)]
for n in range(1, N + 1):
    for m in range(1, M + 1):
        if not S[n][m]:
            continue
        v = 4
        if S[n - 1][m]:
            U[0][n][m] = 1
            v -= 1
        if S[n][m + 1]:
            U[1][n][m] = 1
            v -= 1
        if S[n + 1][m]:
            U[2][n][m] = 1
            v -= 1
        if S[n][m - 1]:
            U[3][n][m] = 1
            v -= 1
        V[n][m] = v

T = [s[:] for s in S]
W = [v[:] for v in V]
for n in range(1, N + 1):
    for m in range(1, M + 2):
        T[n][m] += T[n][m - 1]
        W[n][m] += W[n][m - 1]
for m in range(1, M + 2):
    for n in range(1, N + 2):
        T[n][m] += T[n - 1][m]
        W[n][m] += W[n - 1][m]

del S
del V


U0, U1, U2, U3 = [[u[:] for u in uu] for uu in U]
for n in range(1, N + 1):
    for m in range(1, M + 2):
        U0[n][m] += U0[n][m - 1]
        U2[n][m] += U2[n][m - 1]
for m in range(1, M + 1):
    for n in range(1, N + 2):
        U1[n][m] += U1[n - 1][m]
        U3[n][m] += U3[n - 1][m]


for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())

    nT = T[x2][y2] - T[x2][y1 - 1] - T[x1 - 1][y2] + T[x1 - 1][y1 - 1]
    nW = W[x2][y2] - W[x2][y1 - 1] - W[x1 - 1][y2] + W[x1 - 1][y1 - 1]

    nU0 = U0[x1][y2] - U0[x1][y1 - 1]
    nU2 = U2[x2][y2] - U2[x2][y1 - 1]
    nU3 = U3[x2][y1] - U3[x1 - 1][y1]
    nU1 = U1[x2][y2] - U1[x1 - 1][y2]

    e = nW + nU0 + nU2 + nU3 + nU1
    ans = e // 2 - nT

    print(ans)
