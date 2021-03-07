N, K = map(int, input().split())
ans = 0
for X in range(2, 2*N+1):
    Y = X - K
    if Y<2 or Y>2*N: continue
    nX = X-1 if X<=N else 2*N+1-X
    nY = Y-1 if Y<=N else 2*N+1-Y
    ans += nX*nY
    
print(ans)
