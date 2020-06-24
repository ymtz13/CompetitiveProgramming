N, M = [int(c) for c in input().split()]
a = [int(input()) for _ in range(M)]+[-1]
j=0

dp = [0, 1]

for i in range(N):
    if i+1 == a[j]:
        dp.append(0)
        while i+1==a[j]:
            j+=1
    else:
        dp.append((dp[i]+dp[i+1]) % 1000000007)

print(dp[-1])
