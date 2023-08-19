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
E = [[] for _ in range(N + 1)]
EdgeWeight = [0] * N
for i in range(1, N):
    u, v, w = map(int, input().split())
    E[u].append((v, i))
    E[v].append((u, i))
    EdgeWeight[i] = w
E[0].append((1, 0))
E[1].append((0, 0))

Q = int(input())
Queries = [tuple(map(int, input().split())) for _ in range(Q)]

stack = deque([(0, None, 0, 0, False)])  # q, parent, iedge, depth, isBack
# weight = [None] * N
Parent = [None] * (N + 1)
Depth = [None] * (N + 1)

EdgeIn = [None] * N
EdgeOut = [None] * N

Node = [None] * (N + 1)

cnt = -1

while stack:
    q, parent, iedge, depth, isBack = stack.pop()
    cnt += 1
    if q is None:
        break

    if isBack:
        EdgeOut[iedge] = cnt

    else:
        EdgeIn[iedge] = cnt
        Node[q] = cnt
        Parent[q] = parent
        Depth[q] = depth

        stack.append((parent, None, iedge, None, True))

        for e, jedge in E[q]:
            if e == parent:
                continue
            stack.append((e, q, jedge, depth + 1, False))


P = [Parent]
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
    du = Depth[u]
    dv = Depth[v]

    dok = 0
    dng = min(du, dv) + 1

    while dng - dok > 1:
        dtgt = (dng + dok) // 2

        au = kth_ancestor(u, du - dtgt)
        av = kth_ancestor(v, dv - dtgt)

        if au != av:
            dng = dtgt
        else:
            dok = dtgt

    return kth_ancestor(u, du - dok)


Weight = [0] * (cnt + 10)
for iedge, (edgeIn, edgeOut) in enumerate(zip(EdgeIn, EdgeOut)):
    Weight[edgeIn] = EdgeWeight[iedge]
    Weight[edgeOut] = -EdgeWeight[iedge]


st = SegTree(cnt + 10, lambda x, y: x + y, 0, Weight)

ans = []
for query in Queries:
    t = query[0]

    if t == 1:
        _, i, w = query
        st.update(EdgeIn[i], w)
        st.update(EdgeOut[i], -w)

    if t == 2:
        _, u, v = query
        l = lca(u, v)
        a = (
            st.query(0, Node[u] + 1)
            + st.query(0, Node[v] + 1)
            - st.query(0, Node[l] + 1) * 2
        )
        ans.append(a)


for a in ans:
    print(a)
