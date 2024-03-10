mod = 998244353

N, M = map(int, input().split())

S = [0] * (M + 1)
A = pow(M, N - 1, mod)

P = []
for x in range(M):
    Px = []
    v = 1
    for n in range(N):
        Px.append(v)
        v *= x
        v %= mod
    P.append(Px)

ans = 0
for nl in range(N):
    nr = N - nl - 1
    p = pow(M, nr, mod)

    for m in range(1, M + 1):
        ans += A - S[m] * p
        ans %= mod

        S[m] *= M
        # S[m] += pow(M - m, nl, mod)
        S[m] += P[M - m][nl]
        S[m] %= mod


print(ans)
