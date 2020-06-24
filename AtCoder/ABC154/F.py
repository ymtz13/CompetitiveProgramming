r1, c1, r2, c2 = map(int, input().split())

M = r2+c2+10#1000010
mod = 10**9+7

f    = [1]*M
p = 1
for i in range(1, M):
    p = p*i%mod
    f[i] = p
    #finv[i] = pow(p, mod-2, mod)

finv = [1]*M
p = finv[-1] = pow(f[-1], mod-2, mod)
for i in range(M-2, 0, -1):
    p = p*(i+1)%mod
    finv[i] = p


def comb(n, k):
    return f[n] * finv[n-k] * finv[k] % mod

def count(R,C):
    ret = ((1<<R+C+1)-1) % mod

    for c in range(C):
        x1 = comb(R+c, c)
        x2 = ((1<<C-c)-1) % mod
        ret = (ret-x1*x2) % mod

    for r in range(R):
        x1 = comb(C+r, r)
        x2 = ((1<<R-r)-1) % mod
        ret = (ret-x1*x2) % mod

    return ret

ans = count(r2, c2) + count(r1-1, c1-1) - count(r2, c1-1) - count(r1-1, c2)
ans %= mod
print(ans)
