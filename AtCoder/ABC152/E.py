def factorize(a):
    factors = {}
    v = a
    if v%2==0: factors[2]=0
    while v%2==0:
        v//=2
        factors[2]+=1
    
    p = 3
    while p*p<=a:
        if v%p==0: factors[p] = 0
        while v%p==0:
            v//=p
            factors[p]+=1
        p+=1
    if v>1: factors[v] = 1
    return factors

N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

# calc lcm
lcm = {}
for a in A:
    factors_a = factorize(a)
    for k, v in factors_a.items():
        if k not in lcm or lcm[k]<v: lcm[k] = v

C = 1
for k, v in lcm.items():
    C *= pow(k, v, mod)
    C %= mod

ans = 0
for a in A:
    ans += C * pow(a, mod-2, mod)
    ans %= mod

print(ans)
    
