N, M = map(int, input().split())
EE = [tuple(map(int, input().split())) for _ in range(M)]

E = [[] for _ in range(N)]
for u, v in EE:
    E[u - 1].append(v - 1)
    E[v - 1].append(u - 1)

dp = [1] * N
S = set(range(1, N))
T = [set(0)]

while N - 1 not in T[-1]:
    Snext = set()
    for i in T[-1]:
        v = dp[i]
        for e in E[i]:
            if e in S:
                dp[e] -= v
                if dp[e] <= 0:
                    S.remove(e)
                    Snext.add(e)

    T.add(S)
    S = Snext
