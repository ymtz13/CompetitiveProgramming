N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [a//2 for a in A]

K = []
for i, a in enumerate(A):
    k = 0
    while a%2==0:
        a//=2
        k+=1
    K.append(k)
    A[i] = a

if len(set(K))>1:
    print(0)
    exit()

def gcd(a,b):
    if a>b: a,b = b,a
    while a: a,b=b%a, a
    return b

def lcm(a,b):
    return a*b//gcd(a,b)

l = 1
for a in A:
    l = lcm(l,a)

l *= 2**K[0]
print((M+l)//(l*2))
