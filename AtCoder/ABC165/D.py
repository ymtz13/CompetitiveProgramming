A, B, N = map(int, input().split())

if B<=A:
    ans = 0
    for x in range(min(B, N+1)):
        ans = max(ans, A*x//B-x//B*A)
else:
    x = min(N, B-1)
    ans = A*x//B

print(ans)
        
