N, M = map(int, input().split())
X = set()
Y = set()

ABC = []
for _ in range(N):
    # (A,C)-(B,C)
    A, B, C = map(int, input().split())
    X.add(A)
    X.add(B)
    Y.add(C)
    ABC.append((A,B,C))

DEF = []
for _ in range(M):
    # (D,E)-(D,F)
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

S = [[False]*nY for _ in range(nX)]
T = [[15]*nY for _ in range(nX)]

for a, b, c in ABC:
    xbgn = XD[a]+1
    xend = XD[b]
    yu   = YD[c]
    yd   = yu+1
    for x in range(xbgn, xend+1):
        T[x][yu]-=4
        T[x][yd]-=8

for d, e, f in DEF:
    ybgn = YD[e]+1
    yend = YD[f]
    xl   = XD[d]
    xr   = xl+1
    for y in range(ybgn, yend+1):
        T[xl][y]-=1
        T[xr][y]-=2

x0 = 0
while XL[x0]<0 and x0<nX-2: x0+=1
y0 = 0
while YL[y0]<0 and y0<nY-2: y0+=1

queue = [(x0, y0)]

ans = 0
while queue:
    queue_new = []
    for qx, qy in queue:
        if S[qx][qy]: continue
        S[qx][qy]=True
        if qx==0 or qy==0 or qx==nX-1 or qy==nY-1:
            print('INF')
            exit()

        ans += (XL[qx]-XL[qx-1])*(YL[qy]-YL[qy-1])

        t = T[qx][qy]
        if t&1: queue_new.append((qx+1,qy))
        if t&2: queue_new.append((qx-1,qy))
        if t&4: queue_new.append((qx,qy+1))
        if t&8: queue_new.append((qx,qy-1))

    queue = queue_new


print(ans)
