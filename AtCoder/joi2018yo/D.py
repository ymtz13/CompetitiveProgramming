N = int(input())
L = [int(input()) for _ in range(N)]

INF = 1 << 60

ans = INF
for m in range(1, sum(L) - L[-1] + 1):
    dp = [0]

    for i, l in enumerate(L, 1):
        dp.append(INF)

        s = 0
        for j in range(i):
            if i == N and j == N - 1:
                break
            s += L[i - j - 1]
            if s >= m:
                dp[-1] = min(dp[-1], max(dp[i - j - 1], s - m))

    # print(m, dp)

    ans = min(ans, dp[-1])

print(ans)
