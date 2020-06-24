X = int(input())
dp = [0]*(X+1)
dp[0]=1

for p in range(100,106):
    for i in range(p, X+1):
        dp[i] |= dp[i-p]
print(dp[X])
