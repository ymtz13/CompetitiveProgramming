N = int(input())
X = list(map(int, input()))[::-1]
p = sum(X)

if p==0:
    for _ in range(N):
        print(1)
    exit()

if p==1:
    if X[0]==0:
        ans = [2]
        for n in range(1, N):
            ans.append(1 if X[n]==0 else 0)
    else:
        ans = [0] + [2]*(N-1)

    for a in ans[::-1]:
        print(a)
        
    exit()
    

pp = p+1
rp = []
k = 1
for n in range(N):
    rp.append(k%pp)
    k = k*2%pp

sp = 0
for r,x in zip(rp, X):
    if x==1: sp = (sp+r)%pp
    
pn = p-1
rn = []
k = 1
for n in range(N):
    rn.append(k%pn)
    k = k*2%pn

sn = 0
for r,x in zip(rn, X):
    if x==1: sn = (sn+r)%pn

def popcount(x):
    p = 0
    while x:
        p += x&1
        x>>=1
    return p

def op(x):
    p = popcount(x)
    return x%p

def f(x):
    n = 0
    while x:
        n+=1
        x = op(x)
    return n
    
ans = []
for n,x in enumerate(X):
    if x==0:
        ans.append(1+f((sp+rp[n])%pp))
    else:
        ans.append(1+f((sn-rn[n])%pn))

for a in ans[::-1]:
    print(a)


