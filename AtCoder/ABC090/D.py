N, K = list(map(int, input().split()))
if K==0:
    print(N*N)
    exit()
    
ans = 0
r = 1
for b in range(K+1, N+1):
    ans += (N//b)*r + max((N%b)-K+1 ,0)
    r += 1
    
print(ans)
