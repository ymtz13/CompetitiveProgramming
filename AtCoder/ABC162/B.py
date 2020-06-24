N = int(input())

ans = 0
for i in range(N+1):
    if i%5 and i%3: ans+=i
print(ans)
