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


N = int(input())
X = list(map(int, input().split()))
L = int(input())
Q = int(input())
Queries = [tuple(map(int, input().split())) for _ in range(Q)]

l = 0
P = []

for r, x in enumerate(X[1:], 1):
    while x - X[l] > L:
        l += 1
    P.append((l + 1, r + 1))

tree = Tree(N, P)

for a, b in Queries:
    if a > b:
        a, b = b, a

    ans = 0
    d = 1 << (len(tree.ancestors) - 1)
    for ancestor in reversed(tree.ancestors):
        p = ancestor[b]

        if p is not None and p >= a:
            ans += d
            b = p

        d >>= 1

    if a < b:
        ans += 1

    print(ans)
