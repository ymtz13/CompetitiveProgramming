mod = 998244353

N, M = map(int, input().split())
S = list(map(int, input().split()))

dp = [0] * (N + 10)
dp[0] = 1

for s in S:
    ndp = [0] * (N + 10)

    if s:
        for m, v in enumerate(dp[:-1]):
            if m == M + 1:
                break
            ndp[m + 1] = v
    else:
        for m in range(1, N + 10):
            ndp[m] = dp[m] * m % mod
            if m < M + 1:
                ndp[m] += dp[m - 1] * (M + 1 - m) % mod
                ndp[m] %= mod

    dp = ndp

ans = 0
for v in dp:
    ans += v
    ans %= mod

print(ans)
