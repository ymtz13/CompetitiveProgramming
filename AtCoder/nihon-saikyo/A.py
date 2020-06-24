M, D = list(map(int, input().split()))
ans = 0
for m in range(1,M+1):
    for d in range(1, D+1):
        d1, d10 = d%10, d//10
        if d1>1 and d10>1 and d1*d10==m: ans += 1
print(ans)
