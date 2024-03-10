class UF:
    def __init__(self, N, identity, op, inv):
        self.n = N  # 連結成分の数
        self.uf = [-1] * N  # 親ノードのインデックス（根は木の大きさ）
        self.du = [identity] * N  # 親ノードとのポテンシャル差（根はゼロ）
        self.op = op
        self.inv = inv

    def find(self, x):
        uf = self.uf
        du = self.du

        if uf[x] < 0:
            return x
        p = uf[x]
        uf[x] = self.find(p)
        du[x] = self.op(du[p], du[x])
        return uf[x]

    def size(self, x):
        return -self.uf[self.find(x)]

    def union(self, x, y, r):
        """
        `u(x) = op(u(y), r)` となるように x と y をつなぐ
        """

        x0, y0 = self.find(x), self.find(y)
        if x0 == y0:
            return

        # u(x0) * du(x) = u(x)
        # u(y0) * du(y) = u(y)
        # u(x) = u(y) * r

        # u(x0) = u(x) * du(x)^-1
        # u(y0) = u(y) * du(y)^-1

        # u(y0)^-1 * u(x0) = (u(y) * du(y)^-1)^-1 * u(x) * du(x)^-1
        #                  = du(y) * u(y)^-1 * u(x) * du(x)^-1
        #                  = du(y) * r * du(x)^-1

        # r' = du(y) * r * du(x)^-1
        # u(x0) = u(y0) * r'

        r = self.op(self.op(self.du[y], r), self.inv(self.du[x]))

        if self.size(x0) > self.size(y0):
            x0, y0 = y0, x0
            r = self.inv(r)
        self.uf[y0] += self.uf[x0]
        self.uf[x0] = y0
        self.du[x0] = r
        self.n -= 1


class UF:
    def __init__(self, N):
        self.uf = [-1] * N  # 親ノードのインデックス（根は木の大きさ）
        self.du = [0] * N  # 親ノードとのポテンシャル差（根はゼロ）
        self.n = N  # 連結成分の数

    def find(self, x):
        if self.uf[x] < 0:
            return x
        p = self.uf[x]
        self.uf[x] = self.find(p)
        self.du[x] += self.du[p]  # u(x) - u(x0) = (u(x) - u(p)) + (u(p) - u(x0))
        return self.uf[x]

    def size(self, x):
        return -self.uf[self.find(x)]

    def union(self, x, y, diff):
        """
        `u(x) - u(y) = diff` となるように x と y をつなぐ
        """

        x0, y0 = self.find(x), self.find(y)
        if x0 == y0:
            return

        # u(x0) + du(x) = u(x)
        # u(y0) + du(y) = u(y)
        # u(x)  - u(y)  = diff

        # u(x0) - u(y0) + du(x) - du(y) = u(x) - u(y)

        # u(x0) - u(y0) = diff - (du(x) - du(y))

        diff -= self.du[x] - self.du[y]

        if self.size(x0) > self.size(y0):
            x0, y0 = y0, x0
            diff = -diff
        self.uf[y0] += self.uf[x0]
        self.uf[x0] = y0
        self.du[x0] = diff
        self.n -= 1
