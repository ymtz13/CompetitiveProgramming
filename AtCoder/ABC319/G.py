mod = 998244353

N, M = map(int, input().split())
EE = [tuple(map(int, input().split())) for _ in range(M)]

E = [[] for _ in range(N)]
for u, v in EE:
    E[u - 1].append(v - 1)
    E[v - 1].append(u - 1)

D = [0] * N
D[0] = 1
S = set(range(1, N))
T = {0}
C = [0] * N

while T and S:
    dsum = 0
    for t in T:
        dsum += D[t]
        dsum %= mod

    Snext = set()
    for t in T:
        d = D[t]
        for e in E[t]:
            if e not in S:
                continue
            C[e] += 1
            D[e] -= d
            D[e] %= mod
            if C[e] == len(T):
                Snext.add(e)

    Tnext = S.difference(Snext)

    for s in Snext:
        C[s] = 0
        D[s] = 0

    for t in Tnext:
        D[t] += dsum
        D[t] %= mod

    if N - 1 in Tnext:
        print(D[N - 1])
        exit()

    T = Tnext
    S = Snext

print(-1)
