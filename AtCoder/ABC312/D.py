mod = 998244353

S = input()
N = len(S)

dp = [0] * N
dp[0] = 1

for c in S:
    if c == "(":
        dp_next = [0] + dp[:-1]

    if c == ")":
        dp_next = dp[1:] + [0]

    if c == "?":
        dp_next = [(v1 + v2) % mod for v1, v2 in zip([0] + dp[:-1], dp[1:] + [0])]

    dp = dp_next

print(dp[0])
