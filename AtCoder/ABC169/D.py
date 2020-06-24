N = int(input())

f = {}
p = 2
while p*p<=N:
    if N%p==0: f[p]=0
    while N%p==0:
        N//=p
        f[p]+=1
    p+=1

if N>1: f[N]=1

ans = 0
for v in f.values():
    n = s = 0
    while s<=v:
        n+=1
        s+=n
    ans += n-1

print(ans)
