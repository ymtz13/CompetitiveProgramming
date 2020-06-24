N = int(input())
A = list(map(int, input().split()))

def gcd(a,b):
    if a>b: a,b = b,a
    while a>0:
        a,b = b%a,a
    return b

for i in range(N-1):
    A[i+1] = gcd(A[i],A[i+1])

print(A[-1])
