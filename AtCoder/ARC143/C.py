N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

cntX = 0
cntY = 0
for a in A:
  r = a % (X + Y)
  if r < X: cntX += 1
  if r < Y: cntY += 1

if cntX == N:
  print('Second')
  exit()

if X <= Y:
  print('First')
  exit()

if cntY == N:
  print('First')
  exit()

print('Second')
