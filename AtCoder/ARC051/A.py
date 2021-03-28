x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

def in_circle(x, y):
  dx = x - x1
  dy = y - y1
  d2 = dx*dx + dy*dy
  return d2 <= r*r

def in_square(x, y):
  return x2 <= x and x <= x3 and y2 <= y and y <= y3

print('NO' if (
  in_square(x1+r, y1  ) and
  in_square(x1-r, y1  ) and
  in_square(x1  , y1+r) and
  in_square(x1  , y1-r)
) else 'YES')

print('NO' if (
  in_circle(x2, y2  ) and
  in_circle(x2, y3  ) and
  in_circle(x3, y2) and
  in_circle(x3, y3)
) else 'YES')
