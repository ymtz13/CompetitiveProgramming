from collections import defaultdict

D = { c:v for v, c in enumerate('LRUD') }
XY = [
  (-1,  0),
  (+1,  0),
  ( 0, +1),
  ( 0, -1),
]

K = int(input())
S = list(map(lambda c: D[c], input()))
F = (0, 0)
M = defaultdict(lambda:[None]*4)
for d in S:
  M[F]
  dx, dy = XY[d]
  x, y = F
  while (x, y) in M:
    m = M[(x, y)]
    if m[d]:
      x, y = m[d]
    else:
      x += dx
      y += dy
  M[F][d] = (x + dx, y + dy)
  F = (x, y)

print(x, y)
