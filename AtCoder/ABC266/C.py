P = [tuple(map(int, input().split())) for _ in range(4)]

for i in range(4):
  x0, y0 = P[i]
  x1, y1 = P[(i + 1) % 4]
  x2, y2 = P[(i + 2) % 4]

  dx1 = x1 - x0
  dy1 = y1 - y0
  dx2 = x2 - x1
  dy2 = y2 - y1

  cross = dx1 * dy2 - dy1 * dx2
  if cross < 0:
    print('No')
    exit()

print('Yes')
