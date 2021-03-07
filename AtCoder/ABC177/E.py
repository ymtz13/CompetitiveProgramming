


def factorize(x):
    f = set()
    if x%2==0: f.add(2)
    while x%2==0: x//=2
    
    p = 3
    while x>=p*p:
        if x%p==0: f.add(p)
        while x%p==0: x//=p
        p+=2
    if x>1: f.add(x)
    return f

N = int(input())
A = list(map(int, input().split()))

F = [0]*(10**6+5)

for a in A:
    for f in factorize(a):
        F[f] += 1

m = max(F)
if m<=1:
    print('pairwise coprime')
elif m<N:
    print('setwise coprime')
else:
    print('not coprime')
    
