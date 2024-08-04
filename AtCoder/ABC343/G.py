def z_algo(S: str):
    L = len(S)
    ret = [L]
    i = 1
    jnxt = 0
    while i < L:
        j = jnxt
        while i + j < L and S[j] == S[i + j]:
            j += 1

        ret.append(j)

        jnxt = 0
        for k in range(1, j):
            if k + ret[k] >= j:
                jnxt = j - k
                break
            ret.append(ret[k])

        i = len(ret)

    return ret


N = int(input())
S = list({input() for _ in range(N)})

rm = set()
for i, si in enumerate(S):
    for j, sj in enumerate(S):
        if i == j:
            continue
        if sj in si:
            rm.add(j)

S = [s for i, s in enumerate(S) if i not in rm]
N = len(S)

# print(S, N)

E = [[None] * N for _ in range(N)]

for i, si in enumerate(S):
    for j, sj in enumerate(S):
        if i == j:
            continue

        ss = sj + "_" + si
        z = z_algo(ss)[len(sj) + 1 :]

        e = 0
        for k, zz in enumerate(z[::-1], 1):
            if k == zz:
                e = k

        E[i][j] = len(sj) - e
        # print(si, sj, e, E[i][j])


INF = 1 << 60
V = [INF] * (N << N)
for i, si in enumerate(S):
    V[(1 << i) * N + i] = len(si)

for bb in range(1 << N):
    for t in range(N):
        bt = 1 << t
        if not bb & bt:
            continue

        for f in range(N):
            bf = 1 << f
            if f == t or not bb & bf:
                continue

            V[bb * N + t] = min(V[bb * N + t], V[(bb - bt) * N + f] + E[f][t])

ans = min(V[-N:])
print(ans)
