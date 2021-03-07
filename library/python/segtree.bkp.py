class SegTreeLayer:
    def __init__(self, segsize, function, upper_layer=None, lower_layer=None):
        self.data = []
        self.segsize = segsize
        self.function = function
        self.upper_layer = upper_layer
        self.lower_layer = lower_layer

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

    
        
bottom = SegTreeLayer(1, lambda x,y: x+y)
top = bottom.extend(7, 0)

print(bottom.data)

bottom.update(4, 5)
print(bottom.data)

bottom.update(6, 2)
print(bottom.data)
print(top.data)

print(top.query(0, 4))
print(top.query(2, 5))
print(top.query(3, 6))
print(top.query(4, 7))

