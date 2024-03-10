N = int(input())

P = [tuple(map(int, input().split())) for _ in range(N)]
R = [tuple(map(int, input().split())) for _ in range(N)]
D = [tuple(map(int, input().split())) for _ in range(N - 1)]

INF = 1 << 120

T = 1 << 60

dp = [INF] * (N * N)
dp[0] = T - 1


def pp():
    for i in range(N):
        v = dp[i * N : i * N + N]
        vv = [(z // T, T - 1 - z % T) for z in v]
        print(vv)


for i0 in range(N):
    for j0 in range(N):
        Ni = N - i0
        Nj = N - j0

        v = dp[i0 * N + j0]
        q = v // T
        r = T - 1 - (v % T)
        p = P[i0][j0]

        dist = [INF] * (Ni * Nj)
        dist[0] = 0

        for i in range(Ni - 1):
            dd = dist[i * Nj] + D[i0 + i][j0]
            dist[(i + 1) * Nj] = dd
        for j in range(Nj - 1):
            dd = dist[j] + R[i0][j0 + j]
            dist[j + 1] = dd

        for i in range(1, Ni):
            for j in range(1, Nj):
                di = dist[(i - 1) * Nj + j] + D[i0 + i - 1][j0 + j]
                dj = dist[i * Nj + (j - 1)] + R[i0 + i][j0 + j - 1]
                dd = min(di, dj)
                dist[i * Nj + j] = dd

        for i in range(Ni):
            for j in range(Nj):
                if i == 0 and j == 0:
                    continue

                i1 = i0 + i
                j1 = j0 + j
                dd = dist[i * Nj + j]

                q1 = max(0, (dd - r + p - 1) // p)
                r1 = q1 * p - dd
                v1 = (q + q1) * T + T - 1 - (r + r1)
                # print((i0, j0), (i1, j1), (q, q1, q + q1), (r, r1, r + r1))

                key = i1 * N + j1
                dp[key] = min(dp[key], v1)

                # p*x + r0 >= dd

        # print(i0, j0)
        # pp()
        # for i in range(N):
        #     print(dp[i * N : i * N + N])


print(dp[-1] // T + N * 2 - 2)
