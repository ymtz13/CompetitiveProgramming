N = int(input())
X = [set(input()) for _ in range(N)]
S = [None]*N
for n in range(N//2):
    union = X[n] & X[N-1-n]
    if not union:
        print(-1)
        exit()
    S[n] = S[N-1-n] = list(union)[0]

if N%2==1: S[N//2] = list(X[N//2])[0]

print(''.join(S))
    
