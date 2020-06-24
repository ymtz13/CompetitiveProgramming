N = int(input())
A = list(map(int, input().split()))
sr = sum(A)
sl = 0
ans = 20202020200
for i in range(N-1):
    sl+=A[i]
    sr-=A[i]
    ans = min(ans, abs(sl-sr))
print(ans)
    
