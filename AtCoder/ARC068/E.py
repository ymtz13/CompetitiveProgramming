K = 500

N, M = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(N)]

A = [0] * (M + 10)
D = [0] * (M + 10)

for L, R in LR:
    P = []
    for t in range(1, R + 1):
        l = (L + t - 1) // t
        r = R // t
        if r <= K:
            break
        P.append((l, r))

    rprev = -1
    for l, r in reversed(P):
        l = max(rprev + 1, l)
        if l <= r:
            D[l] += 1
            D[r + 1] -= 1
            rprev = r

    for i in range(1, K + 1):
        q = R // i
        if L <= i * q:
            A[i] += 1

s = 0
S = []
for d in D:
    s += d
    S.append(s)

for i in range(M + 1):
    if i > K:
        A[i] += S[i]

for a in A[1 : M + 1]:
    print(a)
