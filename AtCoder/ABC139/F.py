from math import atan2, pi
from functools import cmp_to_key


def cmp(v1, v2):
  x1, y1 = v1
  x2, y2 = v2
  if y1 * y2 < 0: return y2 - y1
  if y1 == 0 and y2 == 0: return x1 - x2

  c = x2 * y1 - x1 * y2
  if c != 0: return c

  return (x1 - x2) * 100000000 + y1 - y2


N = int(input())
V = [tuple(map(int, input().split())) for _ in range(N)]
#V.sort(key=lambda v: atan2(v[1], v[0]) + pi)
V.sort(key=cmp_to_key(cmp))
print(V)
print(sorted(V[::-1], key=cmp_to_key(cmp)))
assert V == sorted(V[::-1], key=cmp_to_key(cmp))
#print(V)
#exit()
V = V + V
#print(V)

Sx = [0]
Sy = [0]
for x, y in V:
  Sx.append(Sx[-1] + x)
  Sy.append(Sy[-1] + y)

ans = 0
for i in range(len(V)):
  for j in range(i + 1, min(len(V), i + 1 + N)):
    dx = Sx[j] - Sx[i]
    dy = Sy[j] - Sy[i]
    ans = max(ans, dx * dx + dy * dy)

print(ans**0.5)
"""
12
-4 -3
5 0
4 -3
0 -5
3 4
-5 0
-3 4
4 3
-4 3
0 5
-3 -4
3 -4
"""
"""
25
-2 -2
-2 -1
-2 0
-2 1
-2 2
-1 -2
-1 -1
-1 0
-1 1
-1 2
0 -2
0 -1
0 0
0 1
0 2
1 -2
1 -1
1 0
1 1
1 2
2 -2
2 -1
2 0
2 1
2 2
"""