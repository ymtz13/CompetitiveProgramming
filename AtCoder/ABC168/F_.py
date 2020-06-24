N, M = map(int, input().split())
X = set()
Y = set()

ABC = []
for _ in range(N):
    A, B, C = map(int, input().split())
    X.add(A)
    X.add(B)
    Y.add(C)
    ABC.append((A,B,C))

DEF = []
for _ in range(M):
    D, E, F = map(int, input().split())
    X.add(D)
    Y.add(E)
    Y.add(F)
    DEF.append((D,E,F))

XL = sorted(list(X))
YL = sorted(list(Y))

XD = {k:v for v,k in enumerate(XL)}
YD = {k:v for v,k in enumerate(YL)}

nX = len(XL)+1
nY = len(YL)+1

S = [[ 0]*nY for _ in range(nX)]
T = [[15]*nY for _ in range(nX)]

for a, b, c in ABC:
    xbgn = XD[a]+1
    xend = XD[b]
    yu   = YD[c]
    yd   = yu+1
    for x in range(xbgn, xend+1):
        T[x][yu]&=0b1011
        T[x][yd]&=0b0111

for d, e, f in DEF:
    ybgn = YD[e]+1
    yend = YD[f]
    xl   = XD[d]
    xr   = xl+1
    for y in range(ybgn, yend+1):
        T[xl][y]&=0b1110
        T[xr][y]&=0b1101

x0 = y0 = 0
while XL[x0]<0 and x0<nX-2: x0+=1
while YL[y0]<0 and y0<nY-2: y0+=1

queue = [(x0, y0)]
iq = 0

ans = 0
while iq<len(queue):
    qx, qy = queue[iq]
    iq += 1
    
    if S[qx][qy]: continue
    S[qx][qy]=1
    if qx==0 or qy==0 or qx==nX-1 or qy==nY-1:
        ans='INF'
        break

    ans += (XL[qx]-XL[qx-1])*(YL[qy]-YL[qy-1])

    t = T[qx][qy]
    if t&1: queue.append((qx+1,qy))
    if t&2: queue.append((qx-1,qy))
    if t&4: queue.append((qx,qy+1))
    if t&8: queue.append((qx,qy-1))

print(ans)
