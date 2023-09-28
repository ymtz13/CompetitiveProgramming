from collections import defaultdict


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

N, D = map(int, input().split())
T = [tuple(map(int, input().split())) for _ in range(N)]


def f(T):
    X = [0]
    Y = [0]
    for x, y in T:
        for x0, y0 in zip(X[:], Y[:]):
            X.append(x0 + x)
            X.append(x0 - x)
            Y.append(y0 + y)
            Y.append(y0 - y)

    D = defaultdict(lambda: -INF)
    for x, y in zip(X, Y):
        D[x] = max(D[x], y)

    R = list(D.items())
    R.sort()
    return R


T1 = T[: N // 2]
T2 = T[N // 2 :]

R1 = f(T1)
R2 = f(T2) + [(INF, 0)]


st = SegTree(len(R2), max, -INF, [v for _, v in R2])


l = 0
r = 0
ans = 0
for x, y in reversed(R1):
    while R2[l][0] + x < -D:
        l += 1
    while R2[r][0] + x <= D:
        r += 1

    if l == r:
        continue
    v = st.query(l, r)
    ans = max(ans, y + v)


print(ans)
