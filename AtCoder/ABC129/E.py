def modpow(a, n, mod):
    res=1
    while n>0:
        if n & 1:
            res = res * a % mod
        n = n>>1
        a = a * a % mod
    return res


L = input()
n1 = L.count('1')

m=0
d=[]
for i, c in enumerate(reversed(L)):
    if c=='1':
        m+=1
        d.append((i, n1-m))

mod = 10**9+7
s = modpow(2, n1, mod)
for dd in d:
    s += (modpow(3,dd[0],mod) * modpow(2,dd[1],mod)) % mod

print(s % mod)
