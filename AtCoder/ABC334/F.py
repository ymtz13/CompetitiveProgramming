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


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    dx = x1 - x2
    dy = y1 - y2

    return (dx * dx + dy * dy) ** 0.5


N, K = map(int, input().split())
pS = tuple(map(int, input().split()))
P = [tuple(map(int, input().split())) for _ in range(N)]

T = dist(pS, P[0]) + dist(pS, P[-1])
A = []

for p1, p2 in zip(P, P[1:]):
    d12 = dist(p1, p2)
    T += d12
    A.append(dist(p1, pS) + dist(p2, pS) - d12)

st = SegTree(N, 0, min)

for i, a in enumerate(A, 1):
    v = st.query(max(0, i - K), i)
    st.update(i, v + a)

print(st.query(max(0, N - K), N) + T)