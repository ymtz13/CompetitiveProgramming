K, S = list(map(int, input().split()))
ans = 0
for X in range(0, K+1):
    for Y in range(0, K+1):
        Z = S-X-Y
        if Z>=0 and Z<=K: ans+=1
print(ans)
