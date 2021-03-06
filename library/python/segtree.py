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
        self.bottom = self.data[-1]

    def update(self, i, value):
        self.bottom[i] = value
        
        for l in range(self.L-2, -1, -1):
            i//=2
            self.data[l][i] = self.function(*self.data[l+1][i*2:i*2+2])

    def update2(self, i, value):
        function = self.function
        layer = self.bottom
        layer[i] = value
        
        for layer_above in self.data[-2::-1]:
            i >>= 1
            j = i<<1
            layer_above[i] = function(layer[j], layer[j+1])
            layer = layer_above
            
    def query(self, ibgn, iend, l=0):
        ssize = self.segsize[l]
        if ibgn%ssize==0 and iend-ibgn==ssize: return self.data[l][ibgn//ssize]

        imid = ibgn - ibgn%ssize + ssize//2
        if iend<=imid or imid<=ibgn:
            return self.query(ibgn, iend, l+1)
        return self.function(
            self.query(ibgn, imid, l+1),
            self.query(imid, iend, l+1)
        )

    def query2(self, qbgn, qend):
        segs = [(qbgn, qend, 0)]
        vals = []
        for ibgn, iend, l in segs:
            ssize = self.segsize[l]
            if ibgn%ssize==0 and iend-ibgn==ssize:
                vals.append(self.data[l][ibgn//ssize])
                continue

            imid = ibgn - ibgn%ssize + ssize//2
            if iend<=imid or imid<=ibgn:
                segs.append((ibgn, iend, l+1))
            else:
                segs.append((ibgn, imid, l+1))
                segs.append((imid, iend, l+1))

        retval = vals[0]
        for val in vals[1:]: retval = self.function(retval, val)
        return retval

    def query3(self, qbgn, qend):
        segsize = self.segsize
        
        segs = [(qbgn, qend)]
        l = 0
        vals = []

        for l, layer in enumerate(self.data):
            ssize = segsize[l]
            segs_next = []
            for ibgn, iend in segs:
                if ibgn%ssize==0 and iend-ibgn==ssize:
                    vals.append(layer[ibgn//ssize])
                    continue

                imid = ibgn - ibgn%ssize + ssize//2
                if iend<=imid or imid<=ibgn:
                    segs_next.append((ibgn, iend))
                else:
                    segs_next.append((ibgn, imid))
                    segs_next.append((imid, iend))
            segs = segs_next

        function = self.function
        retval = vals[0]
        for val in vals[1:]: retval = function(retval, val)
        return retval        

    def __str__(self):
        s = []
        for l, row in enumerate(self.data):
            s.append('{:2d} {}'.format(l, row))
        return '\n'.join(s)


s = SegTree(10, 0, max)
s.update2(5, 6)
s.update2(9, 7)
s.update2(3, 3)

print(s)

print(s.query(2,6))
print(s.query3(2,6))

for qbgn in range(10):
    for qend in range(qbgn+2, 10):
        v  = s.query (qbgn, qend)
        v3 = s.query3(qbgn, qend)
        assert v==v3, (qbgn, qend, v, v3)
