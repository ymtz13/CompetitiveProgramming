N, C = list(map(int, input().split()))
E = []
for _ in range(N):
    s, t, c = list(map(int, input().split()))
    E.append((s, c, +1))
    E.append((t, c, -1))

E = sorted(E, key=lambda x:-x[2])
E = sorted(E, key=lambda x:x[0])

print(E)
    
n = 0
nmax = 0
ie = 0
X = [0]*31
while ie<len(E):
    t = E[ie][0]
    while ie<len(E) and E[ie][0]==t and E[ie][2]==1:
        c = E[ie][1]
        if X[c]==0: n+=1
        X[c] +=1
        ie+=1

    nmax = max(nmax, n)
        
    while ie<len(E) and E[ie][0]==t and E[ie][2]==-1:
        c = E[ie][1]
        X[c] -= 1
        if X[c]==0: n-=1
        ie+=1

print(nmax)
    
