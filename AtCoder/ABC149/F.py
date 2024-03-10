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


mod = 10**9 + 7

N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

tree = Tree(N, edges)

C = [0] * (N + 1)
for q in reversed(tree.order):
    C[q] += 1
    for e in tree.E[q]:
        C[q] += C[e]

cnt = 0
for q, c in enumerate(C[1:], 1):
    X = []
    for e in tree.E[q]:
        if e == tree.parent[q]:
            continue
        X.append(C[e])

    if q != 1:
        X.append(N - 1 - sum(X))

    if len(X) == 1:
        continue

    c = pow(2, N - 1, mod)
    for x in X:
        c -= pow(2, x, mod)
    c += len(X) - 1

    cnt += c

ans = cnt * pow(pow(2, mod - 2, mod), N, mod) % mod
print(ans)
