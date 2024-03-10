class UF:
    def __init__(self, N):
        self.uf = [-1] * N
        self.potential_diff = [0] * N
        self.n = N

    def find(self, x):
        if self.uf[x] < 0:
            return x
        old_parent = self.uf[x]
        self.uf[x] = self.find(self.uf[x])
        self.potential_diff[x] += self.potential_diff[old_parent]
        return self.uf[x]

    def size(self, x):
        return -self.uf[self.find(x)]

    def union(self, xq, yq, diff):
        # x + d[x] = xq
        # y + d[y] = yq
        # xq - yq = diff

        # x        = yq - d[x] + diff
        # y        = yq - d[y]

        # x - y    = diff - (d[x] - d[y])

        x, y = self.find(xq), self.find(yq)
        if x == y:
            return

        diff -= self.potential_diff[xq] - self.potential_diff[yq]

        if self.size(x) > self.size(y):
            x, y = y, x
            diff = -diff
        self.uf[y] += self.uf[x]
        self.uf[x] = y
        self.potential_diff[x] = diff
        self.n -= 1


N, Q = map(int, input().split())
ABD = [tuple(map(int, input().split())) for _ in range(Q)]

uf = UF(N)

ans = []
for i, (a, b, d) in enumerate(ABD, 1):
    a -= 1
    b -= 1

    ia = uf.find(a)
    ib = uf.find(b)

    if ia == ib:
        if uf.potential_diff[a] - uf.potential_diff[b] != d:
            continue

    else:
        uf.union(a, b, d)

    ans.append(i)

print(*ans)
