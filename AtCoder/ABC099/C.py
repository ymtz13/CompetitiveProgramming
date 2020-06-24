N = int(input())
X = [0]
for n in range(1,N+1):
    x = X[-1]+1
    
    r6 = 6
    while n-r6>=0:
        x = min(x, X[n-r6]+1)
        r6*=6

    r9 = 9
    while n-r9>=0:
        x = min(x, X[n-r9]+1)
        r9*=9

    X.append(x)

print(X[N])
