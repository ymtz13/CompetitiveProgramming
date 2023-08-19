from collections import deque


class Tree:
    def __init__(self, N, edges, root=1):
        E = [[] for _ in range(N + 1)]
        for u, v in edges:
            E[u].append(v)
            E[v].append(u)

        queue = deque([(root, None, 0)])
        parent = [None] * (N + 1)
        depth = [None] * (N + 1)

        while queue:
            q, p, d = queue.popleft()
            parent[q] = p
            depth[q] = d

            for e in E[q]:
                if e == p:
                    continue
                queue.append((e, q, d + 1))

        ancestors = [parent]

        n = N
        while n:
            n >>= 1
            ancestor = ancestors[-1]
            ancestor_next = [None]
            for q in range(1, N + 1):
                p = ancestor[q]
                ancestor_next.append(p and ancestor[p])
            ancestors.append(ancestor_next)

        self.N = N
        self.edges = edges
        self.E = E
        self.parent = parent
        self.depth = depth
        self.ancestors = ancestors

    def ancestorOf(self, q, k):
        for ancestor in self.ancestors:
            if not q:
                break

            if k & 1:
                q = ancestor[q]
            k >>= 1

        return q

    def lca(self, x, y):
        if self.depth[x] > self.depth[y]:
            x, y = y, x

        y = self.ancestorOf(y, self.depth[y] - self.depth[x])

        if x == y:
            return x

        for ancestor in reversed(self.ancestors):
            px = ancestor[x]
            py = ancestor[y]
            if px != py:
                x = px
                y = py

        return self.parent[x]


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
edges = []
for i in range(1, N):
    u, v, w = map(int, input().split())
    E[u].append((v, i))
    E[v].append((u, i))
    EdgeWeight[i] = w
    edges.append((u, v))
E[0].append((1, 0))
E[1].append((0, 0))

tree = Tree(N, edges)

Q = int(input())
Queries = [tuple(map(int, input().split())) for _ in range(Q)]

stack = deque([(0, None, 0, False)])  # q, parent, iedge, isBack

EdgeIn = [None] * N
EdgeOut = [None] * N

Node = [None] * (N + 1)

cnt = -1

while stack:
    q, parent, iedge, isBack = stack.pop()
    cnt += 1
    if q is None:
        break

    if isBack:
        EdgeOut[iedge] = cnt

    else:
        EdgeIn[iedge] = cnt
        Node[q] = cnt

        stack.append((parent, None, iedge, True))

        for e, jedge in E[q]:
            if e == parent:
                continue
            stack.append((e, q, jedge, False))


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
        l = tree.lca(u, v)
        a = (
            st.query(0, Node[u] + 1)
            + st.query(0, Node[v] + 1)
            - st.query(0, Node[l] + 1) * 2
        )
        ans.append(a)


for a in ans:
    print(a)
