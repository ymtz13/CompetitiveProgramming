mod = 998244353

F = [1]
for i in range(1, 4000010):
    F.append(F[-1] * i % mod)


def inv(X):
    return pow(X, mod - 2, mod)


def comb(A, B):
    return F[A] * inv(F[B]) * inv(F[A - B]) % mod


R, G, B, K = map(int, input().split())

R -= K
G -= K

P = F[G + B + K]
for X in (G, B, K):
    P *= inv(F[X])
    P %= mod

Q = comb(R + B + K, R)

print(P * Q % mod)
