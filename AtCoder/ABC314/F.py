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


mod = 998244353


def op(x, y):
    return (x + y) % mod


def inv(x):
    return -x


N = int(input())
PQ = [tuple(map(int, input().split())) for _ in range(N)]

V = [0] * N
uf = UF(N, 0, op, inv)

for p, q in PQ:
    p -= 1
    q -= 1

    sp = uf.size(p)
    sq = uf.size(q)
    d = pow(sp + sq, mod - 2, mod)

    V[p] += sp * d % mod
    V[q] += sq * d % mod
    V[p] %= mod
    V[q] %= mod

    uf.union(p, q)
