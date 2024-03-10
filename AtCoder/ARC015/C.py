from math import gcd


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


N = int(input())
X = [tuple(input().split()) for _ in range(N)]

T = []
D = {}
E = []

for large, m, small in X:
    m = int(m)

    if large not in D:
        i = len(T)
        T.append(large)
        D[large] = i

    if small not in D:
        i = len(T)
        T.append(small)
        D[small] = i

    i = D[large]
    j = D[small]

    E.append((i, j, m))


def op(l, r):
    numL, denomL = l
    numR, denomR = r

    num = numL * numR
    denom = denomL * denomR

    g = gcd(num, denom)
    return (num // g, denom // g)


def inv(x):
    num, denom = x
    return (denom, num)


def diff(l, r):
    numL, denomL = l
    numR, denomR = r

    return numL * denomR - numR * denomL


K = len(T)
uf = UF(K, (1, 1), op, inv)

for i, j, m in E:
    uf.union(i, j, (m, 1))
    # print(uf.uf)
    # print(uf.du)

for i in range(K):
    uf.find(i)

imax = None
vmax = (0, 1)
imin = None
vmin = (1, 0)
for i, v in enumerate(uf.du):
    # print(i, v, uf.find(i))
    if diff(vmax, v) < 0:
        imax = i
        vmax = v
    if diff(vmin, v) > 0:
        imin = i
        vmin = v

print(f"1{T[imax]}={op(vmax, inv(vmin))[0]}{T[imin]}")
