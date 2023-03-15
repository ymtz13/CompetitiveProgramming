from collections import defaultdict

M = 200010
P = [None] * M
for p in range(2, M):
    if P[p] is not None:
        continue
    for x in range(p, M, p):
        P[x] = p


def f(x):
    r = defaultdict(int)
    while x > 1:
        p = P[x]
        r[p] += 1
        x //= p

    return r


def g(x):
    p = f(x)

    r = 1
    for v in p.values():
        r *= v + 1
    return r


N = int(input())

ans = 0
for AB in range(1, N):
    CD = N - AB
    ans += g(AB) * g(CD)

print(ans)
