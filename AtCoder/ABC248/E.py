def gcd(a, b):
  while a:
    a, b = b % a, a
  return b


N, K = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]

if K == 1:
  print('Infinity')
  exit()

L = set()
for i, (x1, y1) in enumerate(P):
  for (x2, y2) in P[i + 1:]:
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
      line = (0, 1, x1, 0)

    elif dy == 0:
      line = (1, 0, 0, y1)

    else:
      if dx < 0:
        dx = -dx
        dy = -dy

      g = gcd(dx, dy)
      dx //= g
      dy //= g

      c = x1 // dx
      line = (dx, dy, x1 - dx * c, y1 - dy * c)

    L.add(line)
    #print('p1 = ({}, {}), p2 = ({}, {}) ==> {}, {}, {}, {}'.format(
    #    x1, y1, x2, y2, *line))

#print(L, len(L))

C = [0] * len(L)

for px, py in P:
  for i, (dx, dy, x0, y0) in enumerate(L):
    ex = px - x0
    ey = py - y0
    if dx * ey == ex * dy: C[i] += 1

#print(C)

ans = 0
for c in C:
  if c >= K: ans += 1

print(ans)
