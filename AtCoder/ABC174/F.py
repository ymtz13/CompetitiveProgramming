class SegTreeLayer:
    def __init__(self, ndata, fill, function, segsize=1,
                 upper_layer=None, lower_layer=None):
        self.data = [fill]*ndata
        self.function = function
        self.segsize = segsize
        self.upper_layer = upper_layer
        self.lower_layer = lower_layer
        
        
        ndata_upper = (ndata+1)//2 if ndata>1 else 0
        if not self.upper_layer and ndata_upper>0:
            self.upper_layer = SegTreeLayer(
                ndata_upper, fill, self.function, self.segsize*2, lower_layer=self)

    def update(self, i, value):
        self.data[i] = value

        if not self.upper_layer: return
        v_upper = vi = self.data[i]
        
        j = i-1 if i&1 else i+1
        if j<len(self.data):
            vj = self.data[j]
            v_upper = self.function(vi, vj)
            
        self.upper_layer.update(i//2, v_upper)

    def query(self, ibgn, iend):
        if ibgn%self.segsize==0 and iend-ibgn==self.segsize:
            return self.data[ibgn//self.segsize]

        imid = (ibgn//self.segsize)*self.segsize + self.segsize//2
        if iend<=imid or imid<=ibgn: return self.lower_layer.query(ibgn, iend)
        return self.function(
            self.lower_layer.query(ibgn, imid),
            self.lower_layer.query(imid, iend)
        )

    def extend(self, add, fill):
        self.data.extend([fill]*add)
        ndata = len(self.data)
        ndata_upper_new = (ndata+1)//2 if ndata>1 else 0
        
        if not self.upper_layer and ndata_upper_new>0:
            self.upper_layer = SegTreeLayer(
                self.segsize*2, self.function, lower_layer=self)

        if self.upper_layer:
            ndata_upper_now = len(self.upper_layer.data)
            return self.upper_layer.extend(ndata_upper_new - ndata_upper_now, fill)

        return self

N, Q = map(int, input().split())
C = list(map(int, input().split()))
LR = sorted([[q]+list(map(int, input().split())) for q in range(Q)], key=lambda x:x[2])

bottom = SegTreeLayer(N, 0, lambda x,y: x+y)
top = bottom
while top.upper_layer: top = top.upper_layer

I = [None]*(N+1)
i = 0
ans = [None]*Q
for q, l, r in LR:
    while i<r:
        bottom.update(i, 1)
        
        c = C[i]
        i_old = I[c]
        if i_old is not None: bottom.update(i_old, 0)
        
        I[c] = i
        i+=1
    ans[q] = top.query(l-1, r)

for a in ans:
    print(a)
