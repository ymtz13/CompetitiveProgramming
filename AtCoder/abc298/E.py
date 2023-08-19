mod = 998244353

N, A, B, P, Q = map(int, input().split())


def f(N, A, P):
    R = [0] * (N + 1)

    prob = [0] * (N + 1)
    prob[A] = 1

    # Pinv = 1 / P
    Pinv = pow(P, mod - 2, mod)

    for cnt in range(1, N + 1):
        prob_next = [0] * (N + 1)

        for f, p in enumerate(prob):
            q = p * Pinv
            for t in range(f + 1, f + P + 1):
                prob_next[min(N, t)] += q
                prob_next[min(N, t)] %= mod

        prob = prob_next
        R[cnt] = prob[N]

    return R


R1 = f(N, A, P)
R2 = f(N, B, Q)


X = [x - y for x, y in zip(R1[1:], R1)]

ans = 0
for x, r2 in zip(X, R2):
    ans += x * (1 - r2)
    ans %= mod

print(ans)
