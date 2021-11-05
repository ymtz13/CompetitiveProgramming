def solve(x, y):
  ax = abs(x)
  ay = abs(y)

  if x == 0: return ay if y > 0 else ay + 1
  if y == 0: return ax + 1 if x > 0 else ax

  if x > 0:
    if y > 0:
      return y - x if y > x else x - y + 2
    else:
      return abs(ax - ay) + 1

  else:
    if y > 0:
      return abs(ax - ay) + 1
    else:
      return y - x if y > x else x - y + 2


x, y = map(int, input().split())
print(solve(x, y))
