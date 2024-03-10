mod = 998244353

N = int(input())

r2 = pow(2, mod - 2, mod)

P = [1]
for n in range(2, N + 1):
    Q = [0]
    s = 0
    for p in P:
        v = Q[-1] * r2 % mod
        v += p * r2 % mod
        v %= mod
        Q.append(v)

        s += v
        s %= mod

    R = 2 * (1 - pow(r2, n, mod))
    Rinv = pow(R, mod - 2, mod)

    r = (1 - s) * Rinv % mod

    rr = r
    for i in range(n):
        Q[i] += r
        Q[i] %= mod
        r = r * r2 % mod

    P = Q

print(*P)
