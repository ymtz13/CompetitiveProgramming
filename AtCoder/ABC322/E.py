INF = 1 << 60

N, K, P = map(int, input().split())
P1 = P + 1
M = P1**K

AC = [tuple(map(int, input().split())) for _ in range(N)]


def decode(s):
    r = []
    for _ in range(K):
        r.append(s % P1)
        s //= P1
    return r


def encode(r):
    s = 0
    for v in reversed(r):
        s *= P1
        s += v
    return s


dp = [INF] * M
dp[0] = 0

for ac in AC:
    c = ac[0]
    a = ac[1:]

    dp_next = dp[:]
    for f in range(M - 1, -1, -1):
        fd = decode(f)
        t = encode([min(P, va + vfd) for va, vfd in zip(a, fd)])
        dp_next[t] = min(dp_next[t], dp_next[f] + c)

    dp = dp_next

print(dp[-1] if dp[-1] < INF else -1)
