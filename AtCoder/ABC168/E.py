N = int(input())
D = {}

def gcd(x,y):
    if x>y: x,y=y,x
    while x:
        x,y=y%x,x
    return y

for _ in range(N):
    A, B = map(int, input().split())
    if   A==0 and B==0: key=(0,0)
    elif A==0: key=(0,1)
    elif B==0: key=(1,0)
    else:
        if A<0:
            A=-A
            B=-B
        g = gcd(A,abs(B))
        key = (A//g, B//g)

    if key not in D: D[key]=0
    D[key]+=1

mod = 10**9+7

ans = 1
n00 = 0
for k1, v1 in D.items():
    if k1==(0,0):
        n00+=v1
        continue
    if v1==0: continue
        
    k2 = (k1[1], -k1[0]) if k1[1]>0 else (-k1[1], k1[0])
    if k2 not in D:
        ans = ans * pow(2, v1, mod) % mod
    else:
        v2 = D[k2]
        m = (pow(2, v1, mod) + pow(2, v2, mod) - 1) % mod
        ans = ans * m % mod
        D[k2]=0
        
print((ans+n00-1)%mod)
