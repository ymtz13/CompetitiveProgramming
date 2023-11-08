N, M = map(int, input().split())
E = [[] for _ in range(N)]

for _ in range(M):
    u, v, b, c = map(int, input().split())
    E[u].append((v, b, c))

ok = 0
ng = 10001

INF = 1 << 60

while ng - ok > 1e-10:
    tgt = (ng + ok) / 2

    dp = [-INF] * (N + 1)
    dp[1] = 0

    for f in range(1, N):
        v = dp[f]

        for t, b, c in E[f]:
            dp[t] = max(dp[t], v + b - tgt * c)

    if dp[-1] >= 0:
        ok = tgt
    else:
        ng = tgt

print(ok)
