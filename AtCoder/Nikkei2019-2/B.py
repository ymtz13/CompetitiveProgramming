N = int(input())
D = list(map(int, input().split()))
M = [0]*N
for d in D: M[d]+=1

if D[0]!=0 or M[0]!=1:
    print(0)
    exit()

ans = 1
mod = 998244353
for i in range(1,N):
    ans *= (M[i-1]**M[i])
    ans %= mod
    
print(ans)
