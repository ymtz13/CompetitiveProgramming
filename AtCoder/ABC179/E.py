N, X, M = map(int, input().split())
D = [-1]*M
A = [X]
for i in range(M):
    if D[X]>=0: break
    D[X] = i
    X = X * X % M    
    A.append(X)

st = D[X]
loop = A[st:-1]

if N<=st:
    ans = sum(A[:N])
else:
    Nl = N-st
    ans = sum(A[:st]) + sum(loop)*(Nl//len(loop)) + sum(loop[:Nl%len(loop)])
print(ans)
