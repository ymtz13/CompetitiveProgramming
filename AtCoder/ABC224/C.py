N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i1, (x1, y1) in enumerate(P):
  for i2, (x2, y2) in enumerate(P[i1 + 1:], i1 + 1):
    for i3, (x3, y3) in enumerate(P[i2 + 1:], i2 + 1):
      vx1 = x2 - x1
      vy1 = y2 - y1
      vx2 = x3 - x1
      vy2 = y3 - y1
      if vx1 * vy2 != vx2 * vy1: ans += 1

print(ans)
