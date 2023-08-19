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


# 1 -+- 2 --- 5
#    +- 3 --- 4 -+- 6 --- 9 --- 10
#    |           +- 7
#    +- 8

tree = Tree(
    10, [(1, 2), (2, 5), (1, 3), (3, 4), (4, 6), (6, 9), (9, 10), (4, 7), (1, 8)]
)

assert tree.N == 10
assert tree.parent == [None, None, 1, 1, 3, 2, 4, 4, 1, 6, 9]
assert tree.depth == [None, 0, 1, 1, 2, 2, 3, 3, 1, 4, 5]
assert tree.ancestors == [
    [None, None, 1, 1, 3, 2, 4, 4, 1, 6, 9],
    [None, None, None, None, 1, 1, 3, 3, None, 4, 6],
    [None, None, None, None, None, None, None, None, None, 1, 3],
    [None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None],
]

assert tree.ancestorOf(10, 0) == 10
assert tree.ancestorOf(10, 1) == 9
assert tree.ancestorOf(10, 2) == 6
assert tree.ancestorOf(10, 3) == 4
assert tree.ancestorOf(10, 4) == 3
assert tree.ancestorOf(10, 5) == 1
assert tree.ancestorOf(10, 6) == None
assert tree.ancestorOf(10, 7) == None

assert tree.lca(5, 8) == 1
assert tree.lca(10, 7) == 4
assert tree.lca(3, 4) == 3
assert tree.lca(10, 10) == 10
assert tree.lca(1, 10) == 1
