N = int(input())
INF = 1 << 60

B = 0
for _ in range(N):
  X, Y, Z = map(int, input().split()) 
  xmin = ymin = zmin = INF
  xmax = ymax = zmax = 0

  M = int(input())
  for _ in range(M):
    x, y, z = map(int, input().split())
    xmin = min(xmin, x)
    xmax = max(xmax, x)
    ymin = min(ymin, y)
    ymax = max(ymax, y)
    zmin = min(zmin, z)
    zmax = max(zmax, z)
  
  B ^= xmin
  B ^= ymin
  B ^= zmin
  B ^= X - 1 - xmax
  B ^= Y - 1 - ymax
  B ^= Z - 1 - zmax

print('WIN' if B else 'LOSE')
