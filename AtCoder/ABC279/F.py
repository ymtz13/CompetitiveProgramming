class UF:
  def __init__(self, N):
    self.uf = [-1] * N
    self.n = N

  def find(self, x):
    if self.uf[x] < 0: return x
    self.uf[x] = self.find(self.uf[x])
    return self.uf[x]

  def size(self, x):
    return -self.uf[self.find(x)]

  def union(self, x, y):
    x, y = self.find(x), self.find(y)
    if x == y: return
    if self.size(x) > self.size(y): x, y = y, x
    self.uf[y] += self.uf[x]
    self.uf[x] = y
    self.n -= 1


_BOX = 0
_BALL = 1

N, Q = map(int, input().split())

M = 2 * N + Q + 10
uf = UF(M)

nextIdx = 2 * N
nextBall = N + 1

boxToIdx = {i + 1: i for i in range(N)}
ballToIdx = {i + 1: i + N for i in range(N)}

idxToBox = {}

for i in range(1, N + 1):
  ibox = boxToIdx[i]

  uf.union(ibox, ballToIdx[i])
  idxToBox[uf.find(ibox)] = i

ans = []

for _ in range(Q):
  op = tuple(map(int, input().split()))
  t = op[0]

  if t == 1:
    _, X, Y = op

    uf.union(boxToIdx[X], boxToIdx[Y])
    idxToBox[uf.find(boxToIdx[X])] = X

    boxToIdx[Y] = nextIdx
    idxToBox[nextIdx] = Y
    nextIdx += 1

  if t == 2:
    _, X = op

    ballToIdx[nextBall] = nextIdx
    uf.union(boxToIdx[X], nextIdx)
    idxToBox[uf.find(boxToIdx[X])] = X

    nextIdx += 1
    nextBall += 1

  if t == 3:
    _, X = op

    ibox = uf.find(ballToIdx[X])
    ans.append(idxToBox[ibox])

for a in ans:
  print(a)
