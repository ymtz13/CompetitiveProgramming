N = int(input())
D = sorted([int(input()) for _ in range(N)])
mod = 10**9+7

S = list(range(1,N+1))

for _ in range(3):
    X = []
    i = -1
    for j, d in enumerate(D):
        while i+1<N and D[i+1]*2<=d: i+=1
        X.append(S[i] if i>=0 else 0)

    s = 0
    S = []
    for x in X:
        s = (s+x)%mod
        S.append(s)
    
print(S[-1])
