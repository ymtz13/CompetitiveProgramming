N, S = map(int, input().split())
A = list(map(int, input().split()))

L = []
l = sl = sr = 0
for a in A:
    sr += a
    while sr - sl > S:
        sl += A[l]
        l += 1

    L.append(l)

dp = []
ans = 0

for i, l in enumerate(L):
    v = i - l + 1

    if l > 0:
        v += dp[l - 1] + l

    dp.append(v)
    ans += v

print(ans)
