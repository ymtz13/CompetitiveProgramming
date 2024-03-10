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
P.sort()

mod = 998244353

Y = [y for _, y in P]
Y.sort()
D = {y: i for i, y in enumerate(Y)}

P = [(i, D[y]) for i, (_, y) in enumerate(P)]

ans = 0

st = SegTree(N + 1, 0, lambda x, y: x + y)

for x, y in P:
    pL = x
    pR = N - 1 - x

    pD = y
    pU = N - 1 - y

    pLU = st.query(y, N + 1)
    pLD = pL - pLU
    pRU = pU - pLU
    pRD = pR - pRU

    kLU = pow(2, pLU, mod) - 1
    kLD = pow(2, pLD, mod) - 1
    kRU = pow(2, pRU, mod) - 1
    kRD = pow(2, pRD, mod) - 1

    kL = pow(2, pL, mod) - 1 - kLU - kLD
    kR = pow(2, pR, mod) - 1 - kRU - kRD
    kU = pow(2, pU, mod) - 1 - kLU - kRU
    kD = pow(2, pD, mod) - 1 - kLD - kRD

    k = pow(2, N, mod) - 1

    k -= kLU + kLD + kRU + kRD
    k -= kL + kR + kU + kD

    ans += k
    ans %= mod

    st.update(y, 1)

print(ans)
