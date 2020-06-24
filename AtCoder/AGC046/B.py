mod = 998244353

A, B, C, D = map(int, input().split())
X = D-B
Y = C-A

# NYI: WHEN X==0 or Y==0
if X==0:
    print(pow(B,Y,mod))
    exit()
    
if Y==0:
    print(pow(A,X,mod))
    exit()  

dp = [B, A]

for x in range(1,X):
    dp.append(dp[-1]*A%mod)

for y in range(1, Y):
    dp_new = [None]*(X+1)
    dp_new[0] = dp[0]*B%mod

    a = 0
    for x in range(1, X+1):
        a = (a+dp[x-1])*(A+y)%mod
        b = dp[x]*(B+x)%mod
        dp_new[x] = (a+b)%mod

    dp = dp_new
        
    
k = 1
ans = 0
for d in dp[::-1]:
    ans += d*k
    ans %= mod
    k *= C
    k %= mod

print(ans)
