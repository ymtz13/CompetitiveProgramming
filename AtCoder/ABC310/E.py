N = int(input())
S = list(map(int, input()))

dp = [0, 0]
ans = 0

for v in S:
    if v == 0:
        dp = [1, sum(dp)]
    else:
        dp = [dp[1], dp[0] + 1]
    ans += dp[1]


print(ans)
