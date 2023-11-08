mod = 10**9 + 7

N = int(input())
X = input()
T = [1 + ord(c) - ord("a") for c in X]

M = 27
Minv = pow(M, mod - 2, mod)

SL = [0]
r = 1
for t in T:
    SL.append((SL[-1] + t * r) % mod)
    r *= M
    r %= mod

SR = [0]
r = 1
for t in T[::-1]:
    SR.append((SR[-1] + t * r) % mod)
    r *= M
    r %= mod


def f(S, L, R):
    v = S[R] - S[L]
    return v * pow(Minv, L, mod) % mod


for i in range(N + 1):
    s0L = f(SL, 0, i)
    s0R = f(SL, i + N, 2 * N)
    s0 = s0L + pow(M, i, mod) * s0R
    s0 %= mod

    s1 = f(SR, N - i, 2 * N - i)

    if s0 == s1:
        ans = X[0:i] + X[i + N : 2 * N]
        if ans[::-1] == X[i : i + N]:
            print(ans)
            print(i)
            exit()

print(-1)
