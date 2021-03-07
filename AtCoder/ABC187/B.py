N = int(input())
XY = sorted([tuple(map(int, input().split())) for _ in range(N)])
ans = 0
for i in range(N):
  for j in range(i+1, N):
    xi, yi = XY[i]
    xj, yj = XY[j]
    if xi==xj: continue
    dx = xj-xi
    dy = yj-yi
    if abs(dy)<=dx: ans += 1

print(ans)