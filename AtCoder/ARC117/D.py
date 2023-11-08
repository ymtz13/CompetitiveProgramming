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
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

tree = Tree(N, edges)

_, root = max([(d, i) for i, d in enumerate(tree.depth[1:], 1)])

tree = Tree(N, edges, root)

depth, start = max([(d, i) for i, d in enumerate(tree.depth[1:], 1)])

onpath = [False] * (N + 1)
i = start
while i:
    onpath[i] = True
    i = tree.parent[i]

# print(root, start, depth, onpath)

nxt = 1
stack = deque([root])
cnt = [None] * (N + 1)
write = False
prevq = None
while stack:
    q = stack.pop()
    forward = True

    # print(stack, q)

    if q < 0:
        forward = False
        q = -q

    if q == start:
        write = True

    if write:
        if cnt[q] is None:
            cnt[q] = nxt
            # print("write", q, nxt)
        if q != prevq:
            nxt += 1

    prevq = q

    if forward:
        childs = deque()
        for e in tree.E[q]:
            if e == tree.parent[q]:
                continue

            if onpath[e]:
                childs.append(-q)
                childs.append(e)
            else:
                childs.appendleft(e)
                childs.appendleft(-q)

        stack.extend(childs)

print(*cnt[1:])
