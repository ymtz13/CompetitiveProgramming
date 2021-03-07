N, K = map(int, input().split())
X = [(i+1, int(x)) for i,x in enumerate(input().split())]

S = [None] + sorted(X, key=lambda x: x[1])
D = [False]*(N+1)

k = K
ans = [None]*(N-K+1)
for i in range(N, K-1, -1):
    ans[i-K] = S[k][0]
    
    if i==K: break
    D[i] = True
    if X[i-1][1]<=k:
        k+=1
        while D[S[k][0]]: k+=1
    
print('\n'.join(map(str, ans)))

    