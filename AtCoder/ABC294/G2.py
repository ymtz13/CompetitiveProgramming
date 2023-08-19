from collections import deque


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


N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    E[u - 1].append((v - 1, w))
    E[v - 1].append((u - 1, w))

stack = deque([(0, 0, None, 0)])
iwpd = [None] * N
idx = [None] * N
weight = [None] * N
parent = [None] * N
depth = [None] * N
i = 0

while stack:
    q, w, p, d = stack.pop()
    iwpd[q] = (i, w, p, d)
    idx[q] = i
    weight[q] = w
    parent[q] = p
    depth[q] = d
    i += 1
    for e, we in reversed(E[q]):
        if e == p:
            continue
        stack.append((e, we, q, d + 1))

rmax = [None] * N
for q, ii in enumerate(idx):
    rmax[q] = ii

print(rmax)

for i, _, p, _ in sorted(iwpd, key=lambda x: -x[3]):
    if p is not None:
        rmax[p] = max(rmax[p], rmax[i])


P = [parent]
for _ in range(17):
    parent = P[-1]
    parent2 = []
    for i, p in enumerate(parent):
        parent2.append(parent[p] if p is not None else None)

    P.append(parent2)


def kth_ancestor(q, k):
    a = q
    for i, p in enumerate(P):
        if k & (1 << i):
            a = p[a]

        if a is None:
            break

    return a


def lca(u, v):
    du = depth[u]
    dv = depth[v]

    dok = 0
    dng = max(du, dv) + 1

    while dng - dok > 1:
        dtgt = (dng + dok) // 2

        au = kth_ancestor(u, du - dtgt)
        av = kth_ancestor(u, dv - dtgt)

        if au != av:
            dng = dtgt
        else:
            dok = dtgt

    return dok


print(idx)
print(weight)
print(P[0])
print(P[1])


st = SegTree(N, lambda x, y: x + y, 0, weight)


ans = []
Q = int(input())
for _ in range(Q):
    query = tuple(map(int, input().split()))
    t = query[0]

    if t == 1:
        _, i, w = query

    if t == 2:
        _, u, v = query
        u -= 1
        v -= 1
        l = lca(u, v)
        a = st.query(0, u + 1) + st.query(0, v + 1) - st.query(0, l + 1) * 2
        print(u, v, l)
        ans.append(a)


for a in ans:
    print(a)
