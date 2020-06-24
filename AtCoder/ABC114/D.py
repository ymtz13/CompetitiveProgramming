N = int(input())

def isPrime(x):
    if x==2: return True
    if x%2==0: return False
    i=3
    while i>0 and i*i<=x:
        if x%i==0: i=-100
        i+=2
    return i>0

P = [p for p in range(2,100) if isPrime(p)]
nP = len(P)

f = [0]*nP

for n in range(1,N+1):
    for ip, p in enumerate(P):
        k = n
        while k%p==0:
            f[ip] += 1
            k//=p
            
r=0
x = [0]*nP
for i in range(nP):
    x[i]=(x[i]+1)*3-1
    for j in range(nP): 
        x[j]=(x[j]+1)*5-1
        for k in range(j,nP):
            x[k]=(x[k]+1)*5-1
            ok=True
            for l in range(nP):
                if x[l] > f[l]:
                    ok = False
                    break
            if ok: r+=1
            x[k]=(x[k]+1)//5-1
        x[j]=(x[j]+1)//5-1
    x[i]=0

print(r)
