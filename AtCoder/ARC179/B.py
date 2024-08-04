mod = 998244353

M, N = map(int, input().split())
X = list(map(int, input().split()))

Z = [0] * M
for i, x in enumerate(X):
    Z[x - 1] |= 1 << i


B = [1 << i for i in range(M)]

dp = [0] * (1 << M)
dp[-1] = 1

for _ in range(N):
    dp_nxt = [0] * (1 << M)

    for f, v in enumerate(dp):
        if v == 0:
            continue

        for i, b in enumerate(B):
            if not f & b:
                continue
            t = (f - b) | Z[i]
            # print(_, f"{f:03b} {t:03b} i:{i} Z[i]:{Z[i]:03b} {v}")
            dp_nxt[t] += v
            dp_nxt[t] %= mod

    dp = dp_nxt

ans = 0
for v in dp:
    ans += v
    ans %= mod

print(ans)
