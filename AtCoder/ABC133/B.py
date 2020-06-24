N, D = [int(c) for c in input().split()]
X = [[int(c) for c in input().split() ] for _ in range(N)]

n=0
for i in range(N):
    for j in range(i+1, N):
        d2 = 0
        for k in range(D):
            diff = X[i][k]-X[j][k]
            d2 += diff * diff
        if int(d2**0.5) * int(d2**0.5) == d2:
            n+=1

print(n)
            
