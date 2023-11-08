from decimal import *

N = int(input())
P = list(map(Decimal, input().split()))

r = Decimal("0.9")

dp = [Decimal("-Infinity")]*(N+1)
dp[0] = Decimal('0')
for j, p in enumerate(P):
    dp_next =dp[:]
    for i, v in enumerate(dp[:j+1]):
        dp_next[i+1]=max(dp_next[i+1], p+v*r)
    dp=dp_next

ans = Decimal("-Infinity")
d = Decimal("0")
for k, v in enumerate(dp[1:], 1):
    d =d*r+Decimal("1")
    a = v/d - Decimal("1200")/(Decimal(k).sqrt())

    ans = max(ans, a)

print(ans)

