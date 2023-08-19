class SegTree:
    def __init__(self, N, function, identity, initialData=None):
        L = 1
        M = 1
        while M < N:
            L += 1
            M <<= 1

        segsize = [1 << l for l in range(L)]
        data = [None] * L

        if initialData:
            layer = data[0] = initialData[:M] + [identity] * (M - len(initialData))
            for i in range(1, L):
                layer = data[i] = [function(*v) for v in zip(layer[0::2], layer[1::2])]

        else:
            for l in range(L):
                data[l] = [identity] * (M // segsize[l])

        self.L = L
        self.segsize = segsize
        self.data = data
        self.function = function
        self.bottom = self.data[0]

        self.zip = [(l, segsize[l], data[l]) for l in range(L)]

    def update(self, i, value):
        function = self.function
        layer = self.bottom
        layer[i] = value

        for layer_above in self.data[1:]:
            i >>= 1
            j = i << 1
            layer_above[i] = function(layer[j], layer[j + 1])
            layer = layer_above

    def query(self, qbgn, qend):
        vals = []
        # segs = []

        q = qbgn
        for l, ssize, data in self.zip:
            if q & ssize and q + ssize <= qend:
                # segs.append((q, ssize))
                vals.append(data[q >> l])
                q += ssize

        for l, ssize, data in reversed(self.zip):
            if q + ssize <= qend:
                # segs.append((q, ssize))
                vals.append(data[q >> l])
                q += ssize

        retval = vals[0]
        for val in vals[1:]:
            retval = self.function(retval, val)

        # return segs
        return retval

    def __str__(self):
        s = []
        for l, row in enumerate(self.data[::-1]):
            s.append("{:2d} {}".format(l, row))
        return "\n".join(s)


INF = 1 << 60

st = SegTree(1 << 20, min, INF)

N = int(input())
B = []
for _ in range(N):
    b = list(map(int, input().split()))
    b.sort(reverse=True)
    B.append(b)
B.sort()

S = set()
for h, w, d in B:
    S.add(h)
    S.add(w)
    S.add(d)
S = list(S)
S.sort()

D = {s: i for i, s in enumerate(S, 1)}

lastZ = INF
tmp = []

for z, x, y in B:
    if lastZ < z:
        for xx, yy in tmp:
            if st.bottom[xx] > yy:
                st.update(xx, yy)
        tmp = []

    lastZ = z
    x = D[x]
    y = D[y]

    m = st.query(0, x)
    if m < y:
        print("Yes")
        exit()

    tmp.append((x, y))

print("No")
