N, M = map(int, input().split())
A = [int(input()) - 1 for _ in range(N)]

S = [[0] for _ in range(M)]
s = [0] * M

for a in A:
    s[a] += 1
    for ss, v in zip(S, s):
        ss.append(v)

L = [0] * (1 << M)
C = [0] * (1 << M)
for b in range(1, 1 << M):
    for i in range(M):
        ii = 1 << i
        if not b & ii:
            continue

        bb = b - ii

        l = L[bb]
        c = C[bb]

        ll = l + S[i][-1]
        cc = c + S[i][ll] - S[i][l]

        L[b] = ll
        C[b] = max(C[b], cc)

print(N - max(C))
