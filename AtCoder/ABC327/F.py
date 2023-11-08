class LazySegTree:
    def __init__(self, N, identity, function, mapping, composition, initial=[]):
        # L = 3, M = 4
        # l=2 : 1
        # l=1 : 10      11
        # l=0 : 100 101 110 111

        L = 1
        M = 1  # N以上の最小の整数
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

        self.lazy = [0] * len(data)
        self.mapping = mapping
        self.composition = composition

        self.seglength = [0]
        for ssize in reversed(self.segsize):
            self.seglength.extend([ssize] * (M // ssize))

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

    def resolve(self, i):
        v = self.lazy[i]

        if v is not None:
            lazy = self.lazy

            if i < self.M:
                j = i << 1
                k = j | 1
                lazy[j] += v
                lazy[k] += v

            data = self.data
            data[i] += v
            lazy[i] = 0

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
        lazy = self.lazy
        resolve = self.resolve
        data = self.data

        segs = self.segments(qbgn, qend)
        ancestors = self.ancestors(segs)

        for i in ancestors:
            resolve(i)

        for i in segs:
            lazy[i] += v

        for i in reversed(ancestors):
            j = i << 1
            resolve(j)
            resolve(j + 1)
            data[i] = max(data[j], data[j + 1])

    def query(self, qbgn, qend):
        resolve = self.resolve
        data = self.data

        segs = self.segments(qbgn, qend)
        ancestors = self.ancestors(segs)

        for i in ancestors:
            resolve(i)

        for i in segs:
            resolve(i)

        retval = data[segs[0]]
        for i in segs[1:]:
            retval = max(retval, data[i])

        return retval

    def query_all(self):
        self.resolve(1)
        return self.data[1]

    def __str__(self):
        s = []
        for l in range(self.L):
            s.append("{:2d} {}".format(l, self.data[1 << l : 2 << l]))
        return "\n".join(s)


N, D, W = map(int, input().split())

M = 200010
E = [[] for _ in range(M)]

TX = [tuple(map(int, input().split())) for _ in range(N)]
for T, X in TX:
    E[T].append(X)
    if T + D < M:
        E[T + D].append(-X)


def mapping(data, lazy, seglength):
    return data + lazy


def composition(lazy0, lazy1):
    return lazy0 + lazy1


lst = LazySegTree(M, 0, max, mapping, composition)

ans = 0
for e in E:
    if not e:
        continue

    for x in e:
        d = 1 if x > 0 else -1
        x = abs(x)
        lst.update(max(1, x - W + 1), x + 1, d)

    ans = max(ans, lst.query_all())

print(ans)
