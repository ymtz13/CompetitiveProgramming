N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
    if a>b: a,b = b,a
    while a: a, b = b%a, a
    return b

ans = A[0]
for a in A[1:]:
    ans = gcd(ans, a)

print(ans)
