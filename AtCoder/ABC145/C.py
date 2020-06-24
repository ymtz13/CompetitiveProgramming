N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
D = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        D[i][j] = D[j][i] = ( (L[i][0]-L[j][0])**2 + (L[i][1]-L[j][1])**2 )**0.5

M = [-1]*N
pathlist = []
def makepath(k, prev):
    if k==8: pathlist.append(M[:])
    for i in range(N):
        if M[i]>=0: continue
        M[i] = k
        makepath(k+1, i)
        M[i] = -1

fact = 1
for i in range(2,N+1): fact*=i
makepath(0, -1)


s = 0
for p in pathlist:
    for i in range(N-1):
        s += D[p[i]][p[i+1]]
        
print(s/len(pathlist))
