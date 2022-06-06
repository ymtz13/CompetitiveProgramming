INF = 1 << 60

N = int(input())
V = [tuple(map(int, input().split())) for _ in range(N)]

M = int(input())
P = [tuple(map(int, input().split())) for _ in range(M)]

Q = int(input())
R = [tuple(map(int, input().split())) for _ in range(Q)]

cnt = [0] * Q

for i in range(N):
  j = (i + 1) % N
  xi, yi = V[i]
  xj, yj = V[j]
  dx, dy = xj - xi, yj - yi

  # rotate 90 degree
  vx, vy = -dy, dx

  dotmax = -INF
  for px, py in P:
    dot = vx * px + vy * py
    if dot > dotmax:
      mpx, mpy = px, py
      dotmax = dot

  ox, oy = xi + mpx, yi + mpy
  for q, (rx, ry) in enumerate(R):
    drx, dry = rx - ox, ry - oy
    dot = vx * drx + vy * dry

    if dot >= 0: cnt[q] += 1

for c in cnt:
  print('Yes' if c == N else 'No')
