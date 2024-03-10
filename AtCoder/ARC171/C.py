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


class Mod:
    def __init__(self, mod, fMax):
        factorial = [1]
        for n in range(1, fMax + 10):
            factorial.append(factorial[-1] * n % mod)

        factorial_inv = [pow(factorial[-1], mod - 2, mod)]
        for n in range(len(factorial) - 1, 0, -1):
            factorial_inv.append(factorial_inv[-1] * n % mod)
        factorial_inv.reverse()

        self.mod = mod
        self.fMax = fMax
        self.factorial = factorial
        self.factorial_inv = factorial_inv

    def comb(self, n, k):
        return (
            self.factorial[n]
            * self.factorial_inv[n - k]
            * self.factorial_inv[k]
            % self.mod
        )


mod = 998244353

mmod = Mod(mod, 10000)

N = int(input())
E = [tuple(map(int, input().split())) for _ in range(N - 1)]

D = [0] * (N + 1)
for l, r in E:
    D[l] += 1
    D[r] += 1

for i, d in enumerate(D):
    if d == 1:
        root = i
        break

tree = Tree(N, E, root)

dp0 = [0] * (N + 1)
dp1 = [0] * (N + 1)

for i in reversed(tree.order):
    childs = [j for j in tree.E[i] if j != tree.parent[i]]

    if not childs:
        dp0[i] = 1
        dp1[i] = 1
        continue

    dp = [0] * (len(childs) + 1)
    dp[0] = 1
    for j in childs:
        v0 = dp0[j]
        v1 = dp1[j]

        ndp = [v * v0 % mod for v in dp]
        for k, v in enumerate(dp[:-1]):
            ndp[k + 1] += v * v1 % mod
            ndp[k + 1] %= mod

        dp = ndp

    s0 = s1 = 0
    for v, f0, f1 in zip(dp, mmod.factorial, mmod.factorial[1:]):
        s0 += v * f0 % mod
        s1 += v * f1 % mod
        s0 %= mod
        s1 %= mod

    dp0[i] = s0
    dp1[i] = s1


ans = dp0[root]
print(ans)
