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


N, Q = map(int, input().split())
A = list(map(int, input().split()))

Query = [[] for _ in range(N + 1)]
for i in range(Q):
    L, R = map(int, input().split())
    Query[R].append((i, L))


M = 500

C = defaultdict(int)
for a in A:
    C[a] += 1

D = {}
E = {}
for k, v in C.items():
    if v > M:
        D[k] = len(D)
    else:
        E[k] = []


S = [[0] for _ in range(len(D))]
for a in A:
    for s in S:
        s.append(s[-1])
    if a in D:
        S[D[a]][-1] += 1

# print(D)
# for s in S:
#    print(s)

st = SegTree(N + 1, lambda x, y: x + y, 0)

ans = [None] * Q

for r, a in enumerate(A, 1):
    if a in E:
        e = E[a]
        e.append(r)
        cnt = 0
        for i in reversed(e):
            st.update(i, cnt * (cnt - 1))
            cnt += 1

        # print(r, e)
        # print(st)
        # print()

    for i, l in Query[r]:
        a = st.query(l, r + 1) // 2
        for s in S:
            cnt = s[r] - s[l - 1]
            a += cnt * (cnt - 1) * (cnt - 2) // 6

        ans[i] = a

for a in ans:
    print(a)
