N = int(input())
AL = [tuple(map(int, input().split())) for _ in range(N)]
mod = int(input())

X = [None]
for d in range(1, 11):
    r = pow(10, d, mod)
    s = 1
    x = []
    for n in range(70):
        x.append(s)
        s += s * r % mod
        s %= mod
        r *= r
        r %= mod
    X.append(x)


ans = 0
s = 0

for a, L in reversed(AL):
    v = 0
    d = len(str(a))
    t = 0
    for i, x in enumerate(X[d]):
        if (L & (1 << i)) == 0:
            continue
        v += x * a * pow(10, t, mod) % mod
        v %= mod
        t += d * (1 << i)

    ans += v * pow(10, s, mod) % mod
    ans %= mod

    s += d * L


print(ans)
