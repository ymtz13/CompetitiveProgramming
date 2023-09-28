N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]


dp = [1 << 60] * (N + 1)
dp[0] = 0

for c in C:
    dp_next = [0]

    for i, d in enumerate(D, 1):
        dp_next.append(min(dp[i], dp[i - 1] + d * c))

    dp = dp_next

print(dp[-1])
