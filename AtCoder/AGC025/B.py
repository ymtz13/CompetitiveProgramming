N, A, B, K = map(int, input().split())
mod = 998244353

f = [None]*(N+1)
f[0] = p = 1
for n in range(1, N+1): f[n] = p = p*n % mod

finv = [None]*(N+1)
finv[N] = p = pow(f[N], mod-2, mod)
for n in range(N-1, -1, -1): finv[n] = p = p*(n+1) % mod

ans = 0
for nA in range(0, N+1):
    sB = K-nA*A
    if sB%B>0: continue
    nB = sB//B
    if nB<0 or nB>N: continue
    xA = f[N] * finv[N-nA] * finv[nA] % mod
    xB = f[N] * finv[N-nB] * finv[nB] % mod
    ans = (ans+xA*xB)%mod

print(ans)
    
    