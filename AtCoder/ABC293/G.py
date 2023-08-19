from collections import defaultdict
from bisect import bisect


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


M = 700

N, Q = map(int, input().split())
A = list(map(int, input().split()))
LR = [tuple(map(int, input().split())) + (i,) for i in range(Q)]
Queries = [[] for _ in range(N + 1)]
for l, r, i in LR:
    Queries[r].append((l, i))

D = defaultdict(list)
for i, a in enumerate(A, 1):
    D[a].append(i)

X = {key: value for key, value in D.items() if len(value) > M}

ans = [0] * Q

st = SegTree(N + 2, lambda x, y: x + y, 0)

for r, a in enumerate(A, 1):
    if a in X:
        continue

    d = D[a]
    j = d.index(r)
    if j >= 2:
        for m, x in enumerate(reversed(d[: j - 1]), 1):
            st.update(x, st.bottom[x] + m)

    for l, iq in Queries[r]:
        ans[iq] += st.query(l, r + 1)

    # print(r, st.bottom)

for l, r, i in LR:
    aa = 0
    for x in X.values():
        cnt = bisect(x, r) - bisect(x, l - 1)
        aa += cnt * (cnt - 1) * (cnt - 2) // 6

    ans[i] += aa

for a in ans:
    print(a)
