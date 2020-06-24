def gcd(a,b):
    while a>0:
        a,b  = b%a, a
    return b

N = int(input())
A = [int(c) for c in input().split()]

gcd_l = []
d = A[0]
for a in A:
    d = gcd(d,a)
    gcd_l.append(d)

gcd_r = []
d = A[-1]
for a in reversed(A):
    d = gcd(d,a)
    gcd_r.append(d)
gcd_r = list(reversed(gcd_r))
    
gcd_a = [gcd_r[1]]
for i in range(1,N-1):
    gcd_a.append(gcd(gcd_l[i-1], gcd_r[i+1]))
gcd_a.append(gcd_l[N-2])

print(max(gcd_a))
