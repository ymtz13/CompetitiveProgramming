mod = 998244353

F = [1]
for i in range(1, 6000):
    F.append(F[-1] * i % mod)

Finv = []
for f in F:
    Finv.append(pow(f, mod - 2, mod))


def comb(n, k):
    if n < k:
        return 0
    return F[n] * Finv[n - k] * Finv[k] % mod


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0

for m, a in enumerate(A, 1):
    mm1 = m - 1
    all = comb(N - 1, mm1)

    r = F[N - m]
    z = a * r % mod

    t = 0
    if mm1 >= 2:
        for k in range(1, K):
            t += comb(N - 2 - k, mm1 - 2)

    for xL in range(N):
        xR = N - 1 - xL

        vL = min(K, xL)
        vR = min(K, xR)

        c0 = comb(N - 1 - vL - vR, mm1)
        c1L = (comb(N - 1 - vL, mm1) - c0) % mod
        c1R = (comb(N - 1 - vR, mm1) - c0) % mod
        c2 = (all - c0 - c1L - c1R) % mod

        ans += (c2 * 2 + c1L + c1R - 1) * z * F[mm1]
        ans %= mod

        print(a, xL, (a, c0, c1L, c1R, c2), r, z, z * F[mm1])

print(ans)


2280 - 540
1740 - 420
1320
