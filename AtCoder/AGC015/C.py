N, M, Q = map(int, input().split())

N2 = N + 2
M2 = M + 2
NM = N2 * M2

S = [0] * NM
for n in range(1, N + 1):
    for m, v in enumerate(map(int, input()), 1):
        S[n * M2 + m] = v


U0 = [0] * NM
U1 = [0] * NM
U2 = [0] * NM
U3 = [0] * NM
V = [0] * NM
for n in range(1, N + 1):
    for m in range(1, M + 1):
        i = n * M2 + m
        if not S[i]:
            continue
        v = 4
        if S[i - M2]:
            U0[i] = 1
            v -= 1
        if S[i + 1]:
            U1[i] = 1
            v -= 1
        if S[i + M2]:
            U2[i] = 1
            v -= 1
        if S[i - 1]:
            U3[i] = 1
            v -= 1
        V[i] = v


for n in range(1, N + 1):
    for m in range(1, M + 2):
        i = n * M2 + m
        S[i] += S[i - 1]
        V[i] += V[i - 1]
for m in range(1, M + 2):
    for n in range(1, N + 2):
        i = n * M2 + m
        S[i] += S[i - M2]
        V[i] += V[i - M2]


for n in range(1, N + 1):
    for m in range(1, M + 2):
        i = n * M2 + m
        U0[i] += U0[i - 1]
        U2[i] += U2[i - 1]
for m in range(1, M + 1):
    for n in range(1, N + 2):
        i = n * M2 + m
        U1[i] += U1[i - M2]
        U3[i] += U3[i - M2]

Queries = [tuple(map(int, input().split())) for _ in range(Q)]

for x1, y1, x2, y2 in Queries:
    x0 = x1 - 1
    y0 = y1 - 1

    nT = S[x2 * M2 + y2] - S[x2 * M2 + y0] - S[x0 * M2 + y2] + S[x0 * M2 + y0]
    nW = V[x2 * M2 + y2] - V[x2 * M2 + y0] - V[x0 * M2 + y2] + V[x0 * M2 + y0]

    nU0 = U0[x1 * M2 + y2] - U0[x1 * M2 + y0]
    nU2 = U2[x2 * M2 + y2] - U2[x2 * M2 + y0]
    nU3 = U3[x2 * M2 + y1] - U3[x0 * M2 + y1]
    nU1 = U1[x2 * M2 + y2] - U1[x0 * M2 + y2]

    e = nW + nU0 + nU2 + nU3 + nU1
    ans = e // 2 - nT

    print(ans)
