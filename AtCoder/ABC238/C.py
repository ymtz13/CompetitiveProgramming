N = int(input())

ans = 0

for k in range(1, 20):
    s = 10 ** (k - 1)
    if s > N:
        break

    t = min(N, s * 10 - 1)
    n = (t - s) + 1
    ans += n * (n + 1) // 2

print(ans % 998244353)
