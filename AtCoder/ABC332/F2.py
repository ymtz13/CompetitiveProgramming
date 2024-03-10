from collections import deque
from time import perf_counter


class LazySegTree:
    def __init__(self, N, identity, function, mapping, composition, initial=[]):
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

        self.lazy = [None] * len(data)
        self.mapping = mapping
        self.composition = composition

        self.seglength = [0]
        self.lbound = [0]
        self.rbound = [0]
        for ssize in reversed(self.segsize):
            self.seglength.extend([ssize] * (M // ssize))
            self.lbound.extend(list(range(0, M, ssize)))
            self.rbound.extend(list(range(ssize, M + 1, ssize)))

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

    def set_lazy(self, i, v):
        lazy = self.lazy
        composition = self.composition

        if lazy[i] is None:
            lazy[i] = v
        else:
            # lazy[i] = composition(lazy[i], v)

            v1, p1 = lazy[i]
            v2, p2 = v
            p = p1 + p2 - p1 * p2
            n = v1 * p1 + v2 * (1 - p1) * p2
            lazy[i] = (n * inv(p), p)

    def resolve(self, i):
        v = self.lazy[i]

        if v is not None:
            lazy = self.lazy

            if i < self.M:
                j = i << 1
                k = j | 1
                # lazyj = lazy[j]
                # lazyk = lazy[k]
                # composition = self.composition
                # lazy[j] = v if lazyj is None else composition(lazyj, v)
                # lazy[k] = v if lazyk is None else composition(lazyk, v)
                self.set_lazy(j, v)
                self.set_lazy(k, v)

            data = self.data

            # data[i] = self.mapping(data[i], v, self.seglength[i])

            v1, p1 = data[i]
            v2, p2 = v
            p = p1 + p2 - p1 * p2
            n = v1 * p1 + v2 * (1 - p1) * p2
            data[i] = (n * inv(p), p)

            lazy[i] = None

    def ancestors(self, segs):
        ancestors = set()
        for i in segs:
            while i > 1:
                i >>= 1
                if i in ancestors:
                    break
                ancestors.add(i)

        return sorted(list(ancestors))

    def update(self, qbgn, qend, v):
        set_lazy = self.set_lazy
        # lazy = self.lazy
        # composition = self.composition
        resolve = self.resolve
        data = self.data
        function = self.function

        segs = self.segments(qbgn, qend)
        ancestors = self.ancestors(segs)

        for i in ancestors:
            resolve(i)

        for i in segs:
            # lazyi = lazy[i]
            # lazy[i] = v if lazyi is None else composition(lazyi, v)
            set_lazy(i, v)

        for i in reversed(ancestors):
            j = i << 1
            resolve(j)
            resolve(j + 1)
            # data[i] = function(data[j], data[j + 1])
            data[i] = data[j]

    def query(self, qbgn, qend):
        resolve = self.resolve
        function = self.function
        data = self.data

        segs = self.segments(qbgn, qend)
        ancestors = self.ancestors(segs)

        for i in ancestors:
            resolve(i)

        for i in segs:
            resolve(i)

        retval = data[segs[0]]
        for i in segs[1:]:
            retval = function(retval, data[i])

        return retval

    def query_all(self):
        self.resolve(1)
        return self.data[1]

    def __str__(self):
        s = []
        for l in range(self.L):
            s.append("{:2d} {}".format(l, self.data[1 << l : 2 << l]))
        return "\n".join(s)


mod = 998244353

N, M = map(int, input().split())
A = list(map(int, input().split()))
Queries = [tuple(map(int, input().split())) for _ in range(M)]


D = {}


def inv(x):
    if x in D:
        return D[x]
    v = pow(x, mod - 2, mod)
    D[x] = v
    return v


def function(l, r):
    return l


def mapping(x1, x2, seglength=1):
    if seglength > 1:
        return (0, 0)
    v1, p1 = x1
    v2, p2 = x2
    p = p1 + p2 - p1 * p2
    n = v1 * p1 + v2 * (1 - p1) * p2
    return (n * inv(p), p)


lst = LazySegTree(N + 1, (0, 0), function, mapping, mapping)


for L, R, X in reversed(Queries):
    K = R - L + 1
    lst.update(L, R + 1, (X, inv(K)))


ans = []
for i, a in enumerate(A, 1):
    v, p = lst.query(i, i + 1)
    q = 1 - p

    z = v * p % mod
    z += a * (1 - p) % mod
    z %= mod

    ans.append(z)

print(*ans)
