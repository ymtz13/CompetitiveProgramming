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


def no():
    print("NO")
    exit()


N = int(input())
A = [0] + list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

tree = Tree(N, edges)

B = A[:]
for q in reversed(tree.order):
    X = [B[c] for c in tree.E[q] if c != tree.parent[q]]

    if len(X) == 0:
        continue

    t = sum(X)
    b = B[q]

    #  p + n = b
    # 2p + n = t
    p = t - b
    n = 2 * b - t
    # print(q, X, t, b, p, n)

    if p < 0 or n < 0:
        no()

    if max(X) * 2 > t and p > t - max(X):
        no()

    B[q] = n

if B[1] > 0 and len(tree.E[1]) > 1:
    no()


print("YES")
