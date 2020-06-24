H, N = map(int, input().split())
dp = [0]*20010
for h in range(1, H+1):
    dp[h] = dp[h], dp[h-1]
