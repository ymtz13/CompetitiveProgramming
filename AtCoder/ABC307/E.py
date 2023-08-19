N, M = map(int, input().split())

mod = 998244353

dp0 = 1
dpX = 0

for i in range(N - 1):
    dp0, dpX = dpX, (dp0 * (M - 1) + dpX * (M - 2)) % mod

print(dpX * M % mod)
