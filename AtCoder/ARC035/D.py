from math import log2


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


N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
Queries = [tuple(map(int, input().split())) for _ in range(Q)]

P = [(0, 0)] + P + [(1000010, 1000010)]

S = [0]
for n in range(1, 2000010):
    S.append(S[-1] + log2(n))


def logBinom(n, k):
    if k == 0 or k == n:
        return 0

    return S[n] - S[n - k] - S[k]


def d(pL, pR):
    xL, yL = pL
    xR, yR = pR
    dx = xR - xL
    dy = yR - yL
    return logBinom(dx + dy, dx)


D = []
for pL, pR in zip(P, P[1:]):
    D.append(d(pL, pR))

st = SegTree(len(D), 0, lambda x, y: x + y, D)

for query in Queries:
    if query[0] == 1:
        _, k, a, b = query
        p = (a, b)

        kL = k - 1
        kR = k + 1

        pL = P[kL]
        pR = P[kR]
        P[k] = p

        st.update(kL, d(pL, p))
        st.update(k, d(p, pR))

    else:
        _, l1, r1, l2, r2 = query

        d1 = st.query(l1, r1)
        d2 = st.query(l2, r2)

        # print(st)
        # print(f"d1={2**d1}, d2={2**d2}")
        print("FIRST" if d1 > d2 else "SECOND")
