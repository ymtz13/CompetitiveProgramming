mod = 998244353

N = int(input())
P = list(map(int, input().split()))

N2 = N * N
F = [0] * N2

for i in range(N):
    F[i * N + i] = 1

for l in range(N - 1, 0, -1):
    ll = l + 1
    pl = P[l]
    for r in range(ll, N):
        f = F[ll * N + r]
        if pl < P[ll]:
            f *= 2
            f %= mod

        for c in range(ll + 1, r + 1):
            if pl > P[c]:
                continue
            vl = F[ll * N + (c - 1)]
            vr = F[c * N + r]

            f += vl * vr % mod
            f %= mod

        F[l * N + r] = f

print(F[N + N - 1])
