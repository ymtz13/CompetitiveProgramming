def distsq(x1, y1, x2, y2):
  dx = x1 - x2
  dy = y1 - y2
  return dx*dx + dy*dy

x, y = map(int, input().split())
N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]
ans = 10**20
for i in range(N):
  x1, y1 = XY[i]
  x2, y2 = XY[(i+1)%N]
  d0 = distsq(x1, y1, x2, y2)
  d1 = distsq(x, y, x1, y1)
  d2 = distsq(x, y, x2, y2)
  d1, d2 = max(d1, d2), min(d1, d2)

  r1 = (d0+d1-d2)/(2*d0**0.5)
  h = (d1-r1*r1)**0.5
  ans = min(ans, h)

print(ans)
