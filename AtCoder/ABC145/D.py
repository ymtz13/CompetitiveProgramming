
X, Y = list(map(int, input().split()))

if (X+Y)%3!=0 or Y<X//2 or Y>X*2:
    print(0)
    exit()

n = (X+Y)//3
k = Y-n  # k = 0...n

mod = 10**9+7

def modpow(n,p,mod):
    retval = 1
    i=0
    while p>>i:
        if (p>>i)&1 : retval = retval*n%mod
        n=n*n%mod
        i+=1
        
    return retval

modfacts = [1]
pre = 1
for i in range(1,n+1):
    pre = pre*i%mod
    modfacts.append(pre)

ans = modfacts[n] * modpow(modfacts[n-k], mod-2, mod) * modpow(modfacts[k], mod-2, mod)
print(ans%mod)
