L, X, Y, S, D = map(int, input().split())

Lr = D-S if D>S else L-(S-D)
Ll = L - Lr
Tr = Lr/(X+Y)
if Y-X<=0:
  print(Tr)
else:
  print(min(Tr, Ll/(Y-X)))
