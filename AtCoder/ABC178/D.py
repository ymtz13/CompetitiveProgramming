mod = 10**9+7

f = [1]
for i in range(1, 2001):
    f.append(f[-1]*i%mod)

S = int(input())
ans = 0
for n in range(1, S//3+1):
    r = S-n*3
    ans += f[r+n-1] * pow(f[n-1], mod-2, mod) * pow(f[r], mod-2, mod) % mod # comb(r+n-1, r)
    ans %= mod
print(ans)
