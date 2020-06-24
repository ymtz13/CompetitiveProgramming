N, P = map(int, input().split())
S = list(map(int, input()))

if P==2 or P==5:
    ans = 0
    for i, s in enumerate(S):
        if s%P==0: ans+=i+1
    print(ans)
    exit()

R = [None]*N
k = 1
for i in range(N-1, -1, -1):
    R[i] = S[i]*k%P
    k = k*10%P

ans = 0
X = []
x = 0
for r in R:
    x  = (x+r)%P
    X.append(x)

D = [0]*P
D[0] = 1
for x in X:
    ans += D[x]
    D[x]+=1

print(ans)
