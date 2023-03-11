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


N, M = map(int, input().split())
X = tuple(map(int, input().split()))
Y = tuple(map(int, input().split()))
ABZ = [tuple(map(int, input().split())) for _ in range(M)]

IX = N
IY = N + 1

T = N + 5
T2 = T * T

E = []
for i, x in enumerate(X):
  E.append(x * T2 + IX * T + i)

for i, y in enumerate(Y):
  E.append(y * T2 + IY * T + i)

for a, b, z in ABZ:
  a -= 1
  b -= 1
  e = z * T2 + a * T + b
  E.append(e)

E.sort()


def solve(x, y):
  uf = UF(N + 2)

  ans = 0

  for e in E:
    cost = e // T2
    r = e % T2
    i = r // T
    j = r % T

    if not x and i == IX: continue
    if not y and i == IY: continue
    if uf.find(i) == uf.find(j): continue

    uf.union(i, j)
    ans += cost

  if uf.n - 2 + x + y > 1:
    return 1 << 60

  return ans


a__ = solve(0, 0)
aX_ = solve(1, 0)
a_Y = solve(0, 1)
aXY = solve(1, 1)

#print(a__, aX_, a_Y, aXY)
print(min(a__, aX_, a_Y, aXY))
