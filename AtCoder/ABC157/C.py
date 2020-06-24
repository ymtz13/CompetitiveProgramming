N, M = map(int, input().split())
ans = [-1]*N

for _ in range(M):
    s, c = map(int, input().split())
    if ans[s-1]==-1: ans[s-1]=c
    elif ans[s-1]!=c:
        print(-1)
        exit()

for k in range(N):
    if ans[k]==-1: ans[k]=1 if k==0 and N>1 else 0

if N>1 and ans[0]==0:
    print(-1)
    exit()
    
print(*ans, sep='')
