N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
  xi, yi = XY[i]
  for j in range(i+1, N):
    xj, yj = XY[j]
    for k in range(j+1, N):
      xk, yk = XY[k]

      dx1, dy1 = xj - xi, yj - yi
      dx2, dy2 = xk - xi, yk - yi
      
      S = abs(dx1*dy2 - dx2*dy1)

      if S>0 and S%2==0: ans += 1

print(ans)
