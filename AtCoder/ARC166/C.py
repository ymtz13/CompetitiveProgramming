mod = 998244353

dp = [1]
v0 = 1
v1 = 0
for _ in range(2000010):
    v0 = v0 + v1
    v1 = v0 - v1
    v0 %= mod
    v1 %= mod
    dp.append((v0 + v1) % mod)

Z = []
z = 1
for i in range(1, 2000008, 2):
    z *= dp[i]
    z %= mod
    Z.append(z)


T = int(input())
cases = [tuple(map(int, input().split())) for _ in range(T)]

ans = []

for H, W in cases:
    if H > W:
        H, W = W, H

    p = pow(Z[H - 1], 2, mod)
    q = pow(dp[2 * H], W - H, mod)
    ans.append(p * q % mod)


for a in ans:
    print(a)
