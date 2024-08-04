mod = 998244353

N, D = map(int, input().split())

F = [1]
Finv = [1]
for i in range(1, D + 10):
    F.append(F[-1] * i % mod)
    Finv.append(pow(F[-1], mod - 2, mod))


def binom(n, k):
    if n < 0 or n < k:
        return 0
    return F[n] * Finv[n - k] * Finv[k] % mod


ans = 1
for k in range(1, D + 2):
    c00 = binom(D - 1, k)
    c01 = binom(D - 1, k - 1)
    c11 = binom(D - 1, k - 2) if k >= 2 else 0
    c10 = c01

    d00 = d11 = 1
    d01 = d10 = 0
    for i in range(50):
        bit = 1 << i
        if N & bit:
            e00 = (d00 * c00 + d01 * c10) % mod
            e01 = (d00 * c01 + d01 * c11) % mod
            e11 = (d10 * c01 + d11 * c11) % mod

            d00 = e00
            d01 = d10 = e01
            d11 = e11

        f00 = (c00 * c00 + c01 * c10) % mod
        f01 = (c00 * c01 + c01 * c11) % mod
        f11 = (c10 * c01 + c11 * c11) % mod

        c00 = f00
        c01 = c10 = f01
        c11 = f11

    ans += d00 + d11
    ans %= mod

print(ans)
