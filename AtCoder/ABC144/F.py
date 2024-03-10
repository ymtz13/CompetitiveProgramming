N, M = map(int, input().split())
E = [[] for _ in range(N)]

for _ in range(M):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    E[s].append(t)

INF = 1 << 60

N5 = N + 5

dp = [INF] * (N5 * N5)


for i in range(N - 2, -1, -1):
    print(i + 1, [e + 1 for e in E[i]])
    s = 0
    v0max = 0
    dmax = 0
    for e in E[i]:
        v0 = V0[e]
        v1 = V1[e]

        s += v0
        v0max = max(v0max, v0)
        dmax = max(dmax, v0 - v1)

    L = len(E[i])

    V0[i] = s / L + 1

    v1 = (s - dmax) / L + 1
    if L > 1:
        v1 = min(v1, (s - v0max) / (L - 1) + 1)
    V1[i] = v1

    print((V0[i], v1))


print(min(V0[0], V1[0]))
