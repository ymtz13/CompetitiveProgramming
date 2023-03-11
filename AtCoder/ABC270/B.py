X, Y, Z = map(int, input().split())

if X < 0:
  X = -X
  Y = -Y
  Z = -Z

if 0 < Y < X:
  if Y < Z:
    print(-1)
  else:
    print(abs(Z) + abs(X - Z))
else:
  print(X)
