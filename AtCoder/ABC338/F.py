INF = 1 << 60

N, M = map(int, input().split())
E = [[INF] * N for _ in range(N)]
D = [[INF] * N for _ in range(N)]

for _ in range(M):
    U, V, W = map(int, input().split())
    E[U - 1][V - 1] = W
    D[U - 1][V - 1] = W


for k in range(N):
    for i in range(N):
        for j in range(N):
            d = D[i][k] + D[k][j]
            if d < D[i][j]:
                D[i][j] = d

ZF = [0] * N
ZT = [0] * N
for i in range(N):
    for j in range(N):
        ZF[i] = min(ZF[i], D[i][j])
        ZT[i] = min(ZT[i], D[j][i])


L = N << N

dp = [INF] * L
for s in range(N):
    dp[(1 << s) * N + s] = ZT[s]

for tt in range(L):
    t = tt % N
    tb = tt // N

    r = 1 << t
    if not tb & r:
        continue
    # print(t, f"{tb:03b}")
    tc = tb - r

    v = dp[tt]
    for f in range(N):
        r = 1 << f
        if tb & r:
            v = min(v, dp[tb * N + f] + D[f][t])
        if tc & r:
            v = min(v, dp[tc * N + f] + D[f][t])

    # print("xxx", t, f"{tb:03b}", f"{tc:03b}", dp[tt], v)
    dp[tt] = v

a = (1 << N) - 1
m = INF
for t in range(N):
    m = min(m, dp[a * N + t] + ZF[t])

# print(m)
print(m if m < INF // 2 else "No")
