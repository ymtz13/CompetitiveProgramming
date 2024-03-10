N, K = map(int, input().split())
WP = [tuple(map(int, input().split())) for _ in range(N)]

INF = 1 << 60


def f(P):
    # (sum wp)/(sum w) > P
    # (sum wp) - (sum w)P > 0
    # sum (wp - wP) > 0

    dp = [-INF] * (K + 1)
    dp[0] = 0

    for w, p in WP:
        v = w * (p - P)
        for k in range(K, 0, -1):
            dp[k] = max(dp[k], dp[k - 1] + v)

    return dp[K] > 0


ok = 0
ng = 101
while ng - ok > 1e-8:
    tgt = (ng + ok) / 2
    if f(tgt):
        ok = tgt
    else:
        ng = tgt

print(ok)
