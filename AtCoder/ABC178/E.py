import sys
sys.setrecursionlimit(2000)

class SegTree:
    def __init__(self, N, fill, function):
        L = 1
        k = 1
        while k<N:
            L += 1
            k<<=1

        segsize = [None]*L
        data = [None]*L
        for l in range(L):
            segsize[l] = 1<<(L-l-1)
            data[l] = [fill]*(1<<l)

        self.L = L
        self.segsize = segsize
        self.data = data
        self.function = function

    def update(self, i, value):
        self.data[self.L-1][i] = value
        for l in range(self.L-2, -1, -1):
            i//=2
            self.data[l][i] = self.function(*self.data[l+1][i*2:i*2+2])

    def query(self, ibgn, iend, l=0):
        ssize = self.segsize[l]
        if ibgn%ssize==0 and iend-ibgn==ssize: return self.data[l][ibgn//ssize]

        imid = ibgn - ibgn%ssize + ssize//2
        if iend<=imid or imid<=ibgn:
            print('return imid', imid, ssize, ibgn)
            return self.query(ibgn, iend, l+1)
        return self.function(
            self.query(ibgn, imid, l+1),
            self.query(imid, iend, l+1)
        )

    def query2(self, qbgn, qend):
        segs = [(qbgn, qend, 0)]
        i = 0
        vals = []
        while i<len(segs):
            ibgn, iend, l = segs[i]
            
            ssize = self.segsize[l]
            if ibgn%ssize==0 and iend-ibgn==ssize: vals.append(self.data[l][ibgn//ssize])

            imid = ibgn - ibgn%ssize + ssize//2
            if iend<=imid or imid<=ibgn:
                segs.append((ibgn, iend, l+1))
            else:
                segs.append((ibgn, imid, l+1))
                segs.append((imid, iend, l+1))

        retval = vals[0]
        for val in vals[1:]: retval = self.function(retval, val)
        return retval
        

    def print(self):
        for l, row in enumerate(self.data):
            print('{:2d} {}'.format(l, row))

S = SegTree(10, 0, max)
S.query(1, 7)

N = int(input())
INF = 10**10
XY = [tuple(map(int, input().split())) for _ in range(N)]

P = sorted(XY)

setY = {y for x, y in P}
lY = sorted(list(setY))
iY = {y:i for i, y in enumerate(lY)}

ans1 = 0
S = SegTree(len(iY), INF, min)
bottom = S.data[-1]

for x, y in P:
    iy = iY[y]
    if bottom[iy]==INF: S.update(iy, x+y)
    
    t = S.query(0, iy+1)
    ans1 = max(ans1, x+y-t)

############################

Z = 10**9+1
P = sorted([(x, Z-y) for x, y in XY])

iY = {Z-y: i for i, y in enumerate(reversed(lY))}

ans2 = 0
S = SegTree(len(iY), INF, min)
bottom = S.data[-1]

for x, y in P:
    iy = iY[y]
    if bottom[iy]==INF: S.update(iy, x+y)
    
    t = S.query(0, iy+1)
    ans2 = max(ans2, x+y-t)

print(max(ans1, ans2))
