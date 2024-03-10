from collections import defaultdict


class SegTree:
    def __init__(self, N, identity, function, initial=[]):
        # L = 3, M = 4
        # l=2 : 1
        # l=1 : 10      11
        # l=0 : 100 101 110 111

        L = 1
        M = 1  # N以上の最小の2冪
        while M < N:
            L += 1
            M <<= 1

        segsize = [1 << l for l in range(L)]

        data = [identity] * M + initial[:M] + [identity] * (M - len(initial))
        if initial:
            for i in range(M - 1, 0, -1):
                j = i << 1
                data[i] = function(data[j], data[j + 1])

        self.L = L
        self.M = M
        self.segsize = segsize
        self.data = data
        self.function = function

        self.zip = [(l, segsize[l]) for l in range(L)]

    def update(self, i, value):
        data = self.data
        function = self.function

        i += self.M
        data[i] = value
        while i > 1:
            i >>= 1
            j = i << 1
            data[i] = function(data[j], data[j + 1])

    def segments(self, qbgn, qend):
        M = self.M

        segs = []

        q = qbgn
        for l, ssize in self.zip:
            if q & ssize and q + ssize <= qend:
                segs.append((q + M) >> l)
                q += ssize

        for l, ssize in reversed(self.zip):
            if q + ssize <= qend:
                segs.append((q + M) >> l)
                q += ssize

        return segs

    def query(self, qbgn, qend):
        function = self.function
        data = self.data

        segs = self.segments(qbgn, qend)

        retval = data[segs[0]]
        for i in segs[1:]:
            retval = function(retval, data[i])

        return retval

    def bottom(self, i):
        return self.data[self.M + i]

    def __str__(self):
        s = []
        for l in range(self.L):
            s.append("{:2d} {}".format(l, self.data[1 << l : 2 << l]))
        return "\n".join(s)


N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(Q)]

init = [(a, 0, 1, 0) for a in A]


def f(lv, rv):
    aL1, aL2, cL1, cL2 = lv
    aR1, aR2, cR1, cR2 = rv

    if aL1 > aR1:
        if aR1 > aL2:
            return (aL1, aR1, cL1, cR1)
        if aR1 < aL2:
            return lv
        if aR1 == aL2:
            return (aL1, aR1, cL1, cR1 + cL2)

    if aR1 > aL1:
        if aL1 > aR2:
            return (aR1, aL1, cR1, cL1)
        if aL1 < aR2:
            return rv
        if aL1 == aR2:
            return (aR1, aL1, cR1, cL1 + cR2)

    if aL1 == aR1:
        if aL2 > aR2:
            return (aL1, aL2, cL1 + cR1, cL2)
        if aR2 > aL2:
            return (aL1, aR2, cL1 + cR1, cR2)
        if aL2 == aR2:
            return (aL1, aL2, cL1 + cR1, cL2 + cR2)


st = SegTree(N, (0, -1, 0, 0), f, init)

for t, p, q in queries:
    if t == 1:
        st.update(p - 1, (q, 0, 1, 0))
    else:
        res = st.query(p - 1, q)
        print(res[3])
