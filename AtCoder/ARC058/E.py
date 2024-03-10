mod = 10**9 + 7

N, X, Y, Z = map(int, input().split())
W = X + Y + Z + 1

M = []
for m in range(1 << W):
    T = []
    for a in range(1, 11):
        t = 1
        for i in range(W):
            if not (m >> i) & 1:
                continue

            j = i + a

            if (i < X and X < j) or (i < X + Y and X + Y < j) or W <= j:
                t |= 1
            else:
                t |= 1 << j

        T.append(t)
    M.append(T)

dp = [0] * (1 << W)
dp[1] = 1
b = 1 << (X + Y + Z)
ans = 0

for n in range(1, N + 1):
    ndp = [0] * (1 << W)

    for m, v in enumerate(dp):
        for t in M[m]:
            ndp[t] += v
            ndp[t] %= mod

    dp = ndp

    for m, v in enumerate(dp):
        if v == 0:
            continue
        s = [i for i in range(W) if (m >> i) & 1]

    p = pow(10, N - n, mod)
    for m, v in enumerate(dp):
        if m & b:
            ans += v * p % mod
            ans %= mod
            dp[m] = 0

print(ans)
