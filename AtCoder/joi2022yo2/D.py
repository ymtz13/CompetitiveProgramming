N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0], [A[0]]]

for i, a in enumerate(A[1:], 2):
    if i > K:
        d = i - K
        for j in range(d + 1, i):
            dp[j][0] = max(dp[j][0], dp[j][d])

        dp[j][0] = max(dp[j][: d + 1])

    dp_next = [v[0] + a for v in dp]
    dp.append(dp_next)

    # print(dp)


ans = 0
for v in dp:
    ans = max(ans, max(v))

print(ans)
