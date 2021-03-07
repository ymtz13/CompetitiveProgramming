N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
ans = 'No'
for i in range(N):
  xi, yi = P[i]
  for j in range(i+1, N):
    xj, yj = P[j]
    dx1, dy1 = xj-xi, yj-yi
    for k in range(j+1, N):
      xk, yk = P[k]
      dx2, dy2 = xk-xi, yk-yi

      if dx1*dy2 == dx2*dy1: ans='Yes'
      

print(ans)