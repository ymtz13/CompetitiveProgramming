N = int(input())
ans = 0
for n in range(1, N+1):
    m = N//n
    ans += n*m*(m+1)//2
print(ans)
