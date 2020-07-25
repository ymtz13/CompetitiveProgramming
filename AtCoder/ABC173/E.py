mod = 10**9+7
def prod(A):
    r = 1
    for a in A:
        r *= abs(a)
        r %= mod
    return r

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), key=abs, reverse=True)

Ak = A[:K]
m = len([a for a in Ak if a<0])

if m%2==0:
    print(prod(Ak))
    exit()

r_p = [a for a in A[K:] if a>=0]
r_n = [a for a in A[K:] if a<=0]
a_p = [a for a in Ak    if a> 0]
a_n_min = max([a for a in Ak if a< 0])

ans1 = ans2 = None
if r_p:
    v1 = abs(a_n_min)
    w1 = max(r_p)
    ans1 = prod(Ak)*pow(v1, mod-2, mod) * w1 % mod
    
if a_p and r_n:
    v2 = min(a_p)
    w2 = abs(min(r_n))
    ans2 = prod(Ak)*pow(v2, mod-2, mod) * w2 % mod
    
if ans1 and ans2:
    print(ans1 if w1*v2>=w2*v1 else ans2)
    exit()

if ans1:
    print(ans1)
    exit()

if ans2:
    print(ans2)
    exit()

print((-prod(A[::-1][:K]))%mod)
