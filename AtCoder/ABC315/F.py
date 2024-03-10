from math import sqrt

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

dp = [1 << 60] * (N * 30)
dp[0] = 0

for i, (xi, yi) in enumerate(P[1:], 1):
    for j in range(max(0, i - 20), i):
        c = i - j - 1

        xj, yj = P[j]
        dx = xi - xj
        dy = yi - yj
        dist = sqrt(dx * dx + dy * dy)

        for ci in range(30):
            cj = ci - c
            if cj < 0:
                continue
            dp[i * 30 + ci] = min(dp[i * 30 + ci], dist + dp[j * 30 + cj])

ans = 1 << 60
for c in range(30):
    p = pow(2, c - 1) if c else 0
    ans = min(ans, dp[(N - 1) * 30 + c] + p)

print(ans)
