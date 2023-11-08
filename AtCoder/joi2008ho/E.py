class UF:
    def __init__(self, N):
        self.uf = [-1] * N
        self.n = N

    def find(self, x):
        if self.uf[x] < 0:
            return x
        self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def size(self, x):
        return -self.uf[self.find(x)]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size(x) > self.size(y):
            x, y = y, x
        self.uf[y] += self.uf[x]
        self.uf[x] = y
        self.n -= 1


W, H = map(int, input().split())
N = int(input())
B = [tuple(map(int, input().split())) for _ in range(N)]

Sx = {-1, W}
Sy = {-1, H}

for x1, y1, x2, y2 in B:
    Sx.add(x1 - 1)
    Sx.add(x1)
    Sx.add(x2 - 1)
    Sx.add(x2)
    Sy.add(y1 - 1)
    Sy.add(y1)
    Sy.add(y2 - 1)
    Sy.add(y2)

Sx = list(Sx)
Sy = list(Sy)
Sx.sort()
Sy.sort()
Dx = {v: i for i, v in enumerate(Sx)}
Dy = {v: i for i, v in enumerate(Sy)}

Mx = Dx[Sx[-1]] + 1
My = Dy[Sy[-1]] + 1
M = Mx * My

S = [0] * M
for x1, y1, x2, y2 in B:
    dx1 = Dx[x1]
    dy1 = Dy[y1]
    dx2 = Dx[x2]
    dy2 = Dy[y2]

    S[dy1 * Mx + dx1] += 1
    S[dy1 * Mx + dx2] -= 1
    S[dy2 * Mx + dx1] -= 1
    S[dy2 * Mx + dx2] += 1

for y in range(0, M, Mx):
    s = 0
    for i, v in enumerate(S[y : y + Mx], y):
        s += v
        S[i] = s

for x in range(Mx):
    s = 0
    for i, v in enumerate(S[x::Mx]):
        s += v
        S[i * Mx + x] = s

# for y in range(My):
#     print(["{: 2}".format(v) for v in S[y * Mx : (y + 1) * Mx]])

xL = Dx[-1]
xR = Dx[W]
yL = Dy[-1]
yR = Dy[H]

yLMx = yL * Mx
yRMx = yR * Mx
for x in range(Mx):
    S[yLMx + x] = S[yRMx + x] = 9
for y in range(0, M, Mx):
    S[y + xL] = S[y + xR] = 9


uf = UF(M)

c0 = S.count(0)
c1 = M - c0

for x in range(Mx - 1):
    for y in range(0, M - 1, Mx):
        i = y + x
        if S[i]:
            continue

        if not S[i + 1]:
            uf.union(i, i + 1)
        if not S[i + Mx]:
            uf.union(i, i + Mx)

print(uf.n - c1)
