def factorize(x):
    f = {}
    for p in range(2, 100000):
        if x%p>0: continue
        f[p] = 0
        while x%p==0:
            f[p]+=1
            x//=p
    if x>1: f[x]=1
    return f

A, B = map(int, input().split())

F = {}
for x in range(B+1,A+1):
    f = factorize(x)
    for k, v in f.items():
        if k not in F: F[k]=0
        F[k] += v

ans = 1
mod = 10**9+7
for k, v in F.items():
    ans = ans * (v+1) % mod

print(ans)
