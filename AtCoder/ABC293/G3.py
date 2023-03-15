from collections import defaultdict


class SegTree:
    def __init__(self, N):
        L = 1
        M = 1
        while M < N:
            L += 1
            M <<= 1

        segsize = [1 << l for l in range(L)]
        data = [None] * L

        for l in range(L):
            data[l] = [0] * (M // segsize[l])

        self.L = L
        self.segsize = segsize
        self.data = data
        self.bottom = self.data[0]

        self.zip = [(l, segsize[l], data[l]) for l in range(L)]

    def update(self, i, value):
        layer = self.bottom
        layer[i] = value

        for layer_above in self.data[1:]:
            i >>= 1
            j = i << 1
            layer_above[i] = layer[j] + layer[j + 1]
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
            retval += val

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


M = 400

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

S = [[0] * len(D)]
Sr = S[0]

st = SegTree(N + 1)

ans = [None] * Q

for r, a in enumerate(A, 1):
    if a in E:
        e = E[a]
        e.append(r)
        cnt = 0
        for i in reversed(e):
            st.update(i, cnt * (cnt - 1))
            cnt += 1

    Sr = Sr[:]
    if a in D:
        Sr[D[a]] += 1
    S.append(Sr)

    for i, l in Query[r]:
        a = st.query(l, r + 1) // 2
        Sl = S[l - 1]
        for sl, sr in zip(Sl, Sr):
            cnt = sr - sl
            a += cnt * (cnt - 1) * (cnt - 2) // 6

        ans[i] = a

for a in ans:
    print(a)
