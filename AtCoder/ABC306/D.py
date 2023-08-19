INF = 1 << 60

N = int(input())

dp0 = 0
dp1 = -INF

for _ in range(N):
    X, Y = map(int, input().split())

    if X == 0:
        dp0 = max(dp0, dp0 + Y, dp1 + Y)

    else:
        dp1 = max(dp1, dp0 + Y)

print(max(dp0, dp1))
