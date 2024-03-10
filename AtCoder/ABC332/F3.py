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


mod = 998244353

N, M = map(int, input().split())
A = list(map(int, input().split()))
Queries = [tuple(map(int, input().split())) for _ in range(M)]

E = [[] for _ in range(N + 5)]
for i, (L, R, X) in enumerate(Queries):
    K = R - L + 1
    E[L].append((X, K, i))
    E[R + 1].append((X, -K, i))


def op(x1, x2):
    v1 = x1 // mod
    p1 = x1 % mod
    v2 = x2 // mod
    p2 = x2 % mod

    if p1 == 0 and p2 == 0:
        return 0

    p = (p1 + p2) % mod
    p -= p1 * p2 % mod
    p %= mod

    n = (v1 * p1 % mod) * (1 - p2) % mod
    n += v2 * p2 % mod
    n %= mod

    return (n * pow(p, mod - 2, mod) % mod) * mod + (p % mod)


# st = SegTree(M + 5, (0, 0), op)
st = SegTree(M + 5, 0, op)


D = {}


def inv(x):
    if x in D:
        return D[x]
    v = pow(x, mod - 2, mod)
    D[x] = v
    return v


ans = []

for a, Ei in zip(A, E[1:]):
    for x, k, m in Ei:
        if k > 0:
            # st.update(m, (x, inv(k)))
            st.update(m, x * mod + pow(p, mod - 2, mod))
        else:
            st.update(m, 0)

    vp = st.query(0, M + 5)
    v = vp // mod
    p = vp % mod

    z = v * p % mod
    z += a * (1 - p) % mod
    z %= mod
    ans.append(z)

print(*ans)
