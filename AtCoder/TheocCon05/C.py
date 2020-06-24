N = int(input())

def gcd(a,b):
    if a<b: a,b=b,a
    while b>0: a, b = b, a%b
    return a

t, a = list(map(int, input().split()))

for _ in range(N-1):
    T, A = list(map(int, input().split()))
    tgt = T*A/(gcd(T,A)**2)
    
