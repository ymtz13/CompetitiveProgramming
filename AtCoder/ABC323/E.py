mod = 998244353

N, X = map(int, input().split())
T = list(map(int, input().split()))

dp = [0] * (20010)
dp[0] = 1

Ninv = pow(N, mod - 2, mod)

t0 = T[0]

ans = 0
for i in range(X + 1):
    p = dp[i]

    for t in T:
        dp[i + t] += p * Ninv
        dp[i + t] %= mod

    if i + t0 > X:
        ans += p * Ninv
        ans %= mod

print(ans)
