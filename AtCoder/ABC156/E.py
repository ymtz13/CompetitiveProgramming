n, k = map(int, input().split())
mod = 10**9+7

R = 200010
f = [1]*R
p = 1
for i in range(1, R):
    p = f[i] = p*i%mod

finv = [1]*R
p = finv[-1] = pow(f[-1], mod-2, mod)
for i in range(R-2, 0, -1):
    p = finv[i] = p*(i+1)%mod

def comb(n, k):
    return f[n]*finv[n-k]*finv[k]%mod
    
ans = 0
for m in range(min(k, n-1)+1):
    x = comb(n, m)
    y = comb(n-1, m)
    ans += x*y%mod

print(ans%mod)
