mod = 998244353

N, K, L = map(int, input().split())

W = N - K + 1
if L < W:
    print(0)
    exit()

ans = 1
for i in range(1, N + 1):
    used = min(W - 1, i - 1)
    ans *= L - used
    ans %= mod

print(ans)
