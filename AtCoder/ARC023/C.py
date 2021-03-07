N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

F = [1]*5000
p = 1
for i in range(1, 5000):
    F[i] = p = p*i%mod

Finv = [1]*5000
Finv[-1] = p = pow(F[-1], mod-2, mod)
for i in range(4999, 1, -1):
    Finv[i-1] = p = p*i%mod

def comb(n, k):
    v = 1
    for i in range(k):
        v = v*(n-i)%mod
    return v*Finv[k]%mod        

ans = 1
b = None
k = 0
X = []
for a in A:
    if a==-1: k+=1
    else:
        if k>0:
            X.append((a-b, k))
            k = 0
        b = a
            
for n, k in X:
    ans = ans * comb(n+k, k) % mod
print(ans)