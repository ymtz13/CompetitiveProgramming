N = int(input())
A = list(map(int, input().split()))
D = {}

ans = 0
for i in range(N):
    s = i-A[i]
    if s in D: ans+=D[s]

    t = i+A[i]
    if t not in D: D[t]=0
    D[t]+=1

print(ans)
    
