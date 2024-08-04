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


from sys import setrecursionlimit

setrecursionlimit(1 << 20)

mod = 998244353

N, H = map(int, input().split())
X = list(map(int, input().split()))

XI = [(x, i) for i, x in enumerate(X)]
XI.sort()

clusters = []
p = -H - 10
for x, i in XI:
    if x - p > H:
        clusters.append([])
    clusters[-1].append(i)
    p = x

V = [0] * N

N5 = N + 5


def f(st, l, r, k):
    if l >= r:
        return

    q = st.query(l, r)
    c = q // N5
    i = q % N5
    n = r - l

    if i == l:
        V[c] += pow(2, n - 1 + k, mod)
        V[c] %= mod
        f(st, l + 1, r, k)
    if i == r - 1:
        V[c] += pow(2, n - 1 + k, mod)
        V[c] %= mod
        f(st, l, r - 1, k)
    if l < i and i < r - 1:
        f(st, l, i, k + (r - 1 - i))
        f(st, i + 1, r, k + (i - l))


CI = [None] * N

for j, cluster in enumerate(clusters):
    n = len(cluster)
    st = SegTree(n, N5, min, [c * N5 + i for i, c in enumerate(cluster)])
    f(st, 0, n, 0)

    for c in cluster:
        CI[c] = j

st = SegTree(len(clusters), 1, lambda x, y: x * y % mod, [0] * len(clusters))

T = [0]
for c, v in enumerate(V):
    i = CI[c]
    st.update(i, (st.bottom(i) + v) % mod)
    T.append(st.query(0, st.M))

ans = [(r - l) % mod for l, r in zip(T, T[1:])]
print(*ans)


# for cluster in clusters:
#     t = 0
#     for c in cluster:
#         t += V[c]
#         t %= mod

#     n = len(cluster)
#     print(cluster, n, t, pow(2, n, mod))
