N, K = map(int, input().split())
A = list(map(int, input().split()))
Am = []
n0 = 0
Ap = []
for a in A:
    if a<0: Am.append(a)
    if a==0: n0+=1
    if a>0: Ap.append(a)

Am = sorted(Am)
Ap = sorted(Ap)
    
nm = len(Am)
np = len(Ap)

Nm = nm*np
N0 = n0*(n0-1)//2 + n0*(nm+np)
Np = nm*(nm-1)//2 + np*(np-1)//2

if K<=Nm:
    # K-th product is negative
    min_ok = 0
    max_ng = -10**20
    while min_ok-max_ng>1:
        tgt = (min_ok+max_ng)//2

        k=0
        i=0
        for a in Am:
            while i<np and a*Ap[i]>tgt: i+=1
            k+=np-i

        if k>=K:
            min_ok = tgt
        else:
            max_ng = tgt
            
    print(min_ok)

elif K<=Nm+N0:
    # K-th product is zero
    print(0)

else:
    # K-th product is positive
    K-= Nm+N0
    
    Am = [-a for a in Am[::-1]]
    
    min_ok = +10**20
    max_ng = 0
    while min_ok-max_ng>1:
        tgt = (min_ok+max_ng)//2

        k=0
        i=np-1
        for j,a in enumerate(Ap):
            while i>=0 and a*Ap[i]>tgt: i-=1
            if i<=j: break
            k+=i-j
            
        i=nm-1
        for j,a in enumerate(Am):
            while i>=0 and a*Am[i]>tgt: i-=1
            if i<=j: break
            k+=i-j
            
        if k>=K:
            min_ok = tgt
        else:
            max_ng = tgt
            
    print(min_ok)
