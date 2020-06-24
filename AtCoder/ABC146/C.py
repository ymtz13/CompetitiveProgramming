A, B, X = list(map(int, input().split()))
if X>=A*(10**9) + B*10:
    print(10**9)
    exit()
for k in range(9,0,-1):
    Y = X-k*B
    n = Y//A
    if n>=10**(k-1):
        print(min(n, 10**k-1))
        exit()
print(0)
