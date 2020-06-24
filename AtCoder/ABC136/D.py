S = input()
N = len(S)

T = [None]*N
X = []
for i in range(N):
    if S[i]=='R':
        X.append(i)
    else:
        for x in X:
            T[x] = i
        X = []

X = []
for i in range(N-1,-1,-1):
    if S[i]=='L':
        X.append(i)
    else:
        for x in X:
            T[x] = i
        X = []

Z = [0]*N
for i in range(N):
    if (T[i]-i)%2==0:
        g = T[i]
    elif S[i]=='R':
        g = T[i]-1
    else:
        g = T[i]+1
    Z[g]+=1

print(*Z)
        
