N, X = list(map(int, input().split()))
W = [int(input()) for _ in range(N)]

W1 = W[:N//2]
W2 = W[N//2:]

def dfs(W, T, i, t):
    if i==len(W):
        T.append(t)
        return
    dfs(W, T, i+1, t)
    dfs(W, T, i+1, t+W[i])

def count(T):
    prev = None
    U = []
    V = []
    for t in T:
        if t!=prev:
            U.append(t)
            V.append(1)
            prev = t
        else:
            V[-1]+=1
    return U,V

    
T1 = []
T2 = []
dfs(W1, T1, 0, 0)
dfs(W2, T2, 0, 0)
U1, V1 = count(sorted(T1))
U2, V2 = count(sorted(T2, reverse=True))

ans = 0
i2 = 0
for u1, v1 in zip(U1, V1):
    while i2<len(U2):
        s = u1 + U2[i2]
        if s<X: break
        if s==X: ans+=v1*V2[i2]
        i2+=1

print(ans)
