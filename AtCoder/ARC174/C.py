mod = 998244353

N = int(input())
Nsqinv = pow(N * N, mod - 2, mod)

X = [0] * (N + 5)

for n in range(N - 1, -1, -1):
    p00 = Nsqinv * n * n % mod
    p01 = Nsqinv * n * (N - n) % mod
    p10 = Nsqinv * (N - n) * (n + 1) % mod
    p11 = Nsqinv * (N - n) * (N - n - 1) % mod

    v00 = p00
    v01 = p01 * (X[n + 1] + 1) % mod
    v10 = p10 * X[n + 1] % mod
    v11 = p11 * X[n + 2] % mod

    v = (v00 + v01 + v10 + v11) % mod

    denom = (1 - p00) % mod

    X[n] = v * pow(denom, mod - 2, mod) % mod


print(*X[:2])
