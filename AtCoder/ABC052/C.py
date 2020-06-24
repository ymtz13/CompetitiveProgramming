N = int(input())
F = {}
for n in range(2,N+1):
    _n = n
    f = 2
    while f*f<=_n:
        if n%f==0 and f not in F: F[f] = 0
        while n%f==0:
            n//=f
            F[f]+=1
        f+=1
    if n>1:
        if n not in F: F[n] = 0
        F[n] += 1

ans = 1
mod = 10**9+7
for _, k in F.items():
    ans = ans*(k+1)%mod
print(ans)
        
        
