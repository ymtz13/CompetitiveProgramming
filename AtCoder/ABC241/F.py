from collections import deque, defaultdict
from bisect import bisect

H, W, N = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())

OX = defaultdict(list)
OY = defaultdict(list)

for _ in range(N):
  X, Y = map(int, input().split())
  OX[Y].append(X)
  OY[X].append(Y)

for ox in OX.values():
  ox.sort()
for oy in OY.values():
  oy.sort()

M = 10**10
gkey = gx * M + gy

D = {}
queue = deque([(sx, sy, 0)])
while queue:
  px, py, d = queue.popleft()
  key = px * M + py

  if key in D: continue
  D[key] = d

  if key == gkey:
    print(d)
    exit()

  a = OX[py]
  i = bisect(a, px)
  # to left
  if i > 0:
    queue.append((a[i - 1] + 1, py, d + 1))

  # to right
  if i < len(a):
    queue.append((a[i] - 1, py, d + 1))

  a = OY[px]
  i = bisect(a, py)
  # to top
  if i > 0:
    queue.append((px, a[i - 1] + 1, d + 1))
  # to bottom
  if i < len(a):
    queue.append((px, a[i] - 1, d + 1))

print(-1)
