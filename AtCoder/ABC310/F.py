mod = 998244353
K = [11, 6, 4, 3, 3, 2, 2, 2, 2, 2]

M = 1
for k in K:
    M *= k


def encode(C):
    r = 0
    for c, k in zip(C[1:], K):
        r *= k
        r += c
    return r


def decode(R):
    C = []
    for k in reversed(K):
        C.append(R % k)
        R //= k
    C.append(0)
    return C[::-1]


# print(encode([0] * 11))
# print(encode([0, 10, 5, 3, 2, 2, 1, 1, 1, 1, 1]))
# print(decode(encode([0, 9, 4, 3, 2, 1, 1, 1, 1, 1, 1])))
# print(decode(encode([0, 5, 3, 2, 1, 1, 0, 1, 1, 0, 1])))

E = [list(range(M)) for _ in range(10)] + [[1] * M]

T = []

for f in range(M):
    C = decode(f)
    dp = [0] * 12
    dp[0] = 1
    for n, c in enumerate(C):
        for _ in range(c):
            dp_next = dp[:]
            for i, v in enumerate(dp):
                dp_next[min(11, i + n)] |= v
            dp = dp_next

    T.append(dp[10])

    for i in range(1, 10):
        if C[i] < K[i - 1] - 1:
            CC = C[:]
            CC[i] += 1
            E[i][f] = encode(CC)


# print(E[4][encode([0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0])])
# print(decode(E[4][encode([0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0])]))

N = int(input())
A = list(map(int, input().split()))

dp = [0] * M
dp[0] = 1

p = 1
for a in A:
    p *= a
    p %= mod

    ov = max(0, a - 10)
    dp_next = [v * ov % mod for v in dp]

    for i in range(1, min(10, a) + 1):
        for t, v in zip(E[i], dp):
            dp_next[t] += v
            dp_next[t] %= mod

    dp = dp_next

s = 0
for t, v in zip(T, dp):
    if t:
        s += v
        s %= mod

ans = s * pow(p, mod - 2, mod) % mod
print(ans)
