N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

# pX, pY, nX, nY = 0, 1, 2, 3
vX = 0
vY = 1
oX = oY = 0

S = [(oX, oY, vX, vY)]

M = int(input())
for _ in range(M):
  op = tuple(map(int, input().split()))
  if len(op)==1:
    t, = op

    if t==1:
      oX, oY = +oY, -oX
      vX = (vX-1)%4
      vY = (vY-1)%4

    else:
      oX, oY = -oY, +oX
      vX = (vX+1)%4
      vY = (vY+1)%4

  else:
    t, p = op

    if t==3:
      oX = 2*p - oX
      if vX%2==0: vX = (vX+2)%4
      if vY%2==0: vY = (vY+2)%4

    else:
      oY = 2*p - oY
      if vX%2==1: vX = (vX+2)%4
      if vY%2==1: vY = (vY+2)%4
  
  S.append((oX, oY, vX, vY))

V = [
  (+1,  0),
  ( 0, +1),
  (-1,  0),
  ( 0, -1),
]

Q = int(input())
for _ in range(Q):
  A, B = map(int, input().split())
  oX, oY, vX, vY = S[A]
  pX, pY = XY[B-1]
  X = oX + pX * V[vX][0] + pY * V[vY][0]
  Y = oY + pX * V[vX][1] + pY * V[vY][1]
  print(X, Y)
  
