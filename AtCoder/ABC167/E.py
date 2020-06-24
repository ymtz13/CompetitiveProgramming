N, M, K = map(int, input().split())

if M==1:
    print(1 if K==N-1 else 0)
    exit()

mod = 998244353

f = [0]*N
f[0] = p = 1
for i in range(1,N):
    f[i] = p = p*i%mod

finv = [0]*N
finv[N-1] = p = pow(f[N-1],mod-2,mod)
for i in range(N-2, -1, -1):
    finv[i] = p = p*(i+1)%mod

ans = 0
for k in range(K+1):
    x = M * pow(M-1, N-k-1, mod) % mod
    y = (f[N-1]*finv[N-1-k]%mod)*finv[k]%mod
    ans = (ans + x*y%mod)%mod

print(ans)
