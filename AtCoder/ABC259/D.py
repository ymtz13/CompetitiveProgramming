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


N = int(input())
sx, sy, tx, ty = map(int, input().split())
C = [tuple(map(int, input().split())) for _ in range(N)]
S = []
T = []

uf = UF(N)

for i, (x, y, r) in enumerate(C):
  dsx = sx - x
  dsy = sy - y
  dtx = tx - x
  dty = ty - y
  if dsx * dsx + dsy * dsy == r * r: S.append(i)
  if dtx * dtx + dty * dty == r * r: T.append(i)

  for j, (xj, yj, rj) in enumerate(C[i + 1:], i + 1):
    dx = xj - x
    dy = yj - y
    d2 = dx * dx + dy * dy

    if d2 < max(r, rj)**2:
      if d2 >= (r - rj)**2:
        uf.union(i, j)

    else:
      if d2 <= (r + rj)**2:
        uf.union(i, j)

ans = 'No'
for s in S:
  for t in T:
    if uf.find(s) == uf.find(t):
      ans = 'Yes'

print(ans)