A,P=[1],[1]
for i in range(50):
    A.append(A[i]*2+3)
    P.append(P[i]*2+1)

def n(N, X):
    if X<=0: return 0
    if N==0: return 1
    return n(N-1, X-1) if X <= A[N-1]+1 else P[N-1] + 1 + n(N-1, X-(A[N-1]+2))

print(n(*list(map(int, input().split()))))
