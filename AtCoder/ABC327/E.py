N = int(input())
P = list(map(int, input().split()))

dp = [-(1<<60)]*(N+1)
dp[0] = 0
for j, p in enumerate(P):
    dp_next =dp[:]
    for i, v in enumerate(dp[:j+1]):
        dp_next[i+1]=max(dp_next[i+1], p+v*0.9)
    dp=dp_next

ans = -(1<<60)
d = 0
for k, v in enumerate(dp[1:], 1):
    d =d*0.9+1
    a = v/d - 1200/(k**0.5)

    ans = max(ans, a)

print(ans)

