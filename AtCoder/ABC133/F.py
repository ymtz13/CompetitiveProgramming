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
        order = []

        while queue:
            q, p, d = queue.popleft()
            parent[q] = p
            depth[q] = d
            order.append(q)

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
        self.order = order
        self.ancestors = ancestors

        stack = deque([(root, 0)])
        pre_order = []
        while stack:
            q, d = stack.pop()
            pre_order.append((q, d))
            if d == 0:
                stack.append((q, 1))
                for e in reversed(E[q]):
                    if e == parent[q]:
                        continue
                    stack.append((e, 0))
        self.pre_order = pre_order

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


N, Q = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

tree = Tree(N, [edge[:2] for edge in edges])

C = [None] * (N + 1)
D = [0] * (N + 1)
for a, b, c, d in edges:
    if tree.depth[a] < tree.depth[b]:
        C[b] = c
        D[b] = d
    else:
        C[a] = c
        D[a] = d


queries = [tuple(map(int, input().split())) for _ in range(Q)]

Z = [[] for _ in range(N + 1)]

for i, (x, y, u, v) in enumerate(queries):
    w = tree.lca(u, v)

    Z[u].append((i, 0, x, y))
    Z[v].append((i, 1, x, y))
    Z[w].append((i, 2, x, y))

R = [[None, None, None] for _ in range(Q)]

CX = [0] * N
DX = [0] * N
dist = 0

for q, o in tree.pre_order:
    if q != 1:
        c = C[q]
        d = D[q]
        if o == 0:
            CX[c] += 1
            DX[c] += d
            dist += d
        else:
            CX[c] -= 1
            DX[c] -= d
            dist -= d

    if o == 0:
        for i, t, x, y in Z[q]:
            r = dist + CX[x] * y - DX[x]
            R[i][t] = r


ans = []
for d0, d1, d2 in R:
    ans.append(d0 + d1 - d2 * 2)

for a in ans:
    print(a)
