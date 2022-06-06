P = [1] * 1000
for p in range(2, 1000):
  if P[p] > 1: continue
  for x in range(p * 2, 1000, p):
    P[x] = p

A, B, C, D = map(int, input().split())
for X in range(A, B + 1):
  f = False
  for Y in range(C, D + 1):
    if P[X + Y] == 1:
      f = True
      break
  if not f:
    print('Takahashi')
    exit()

print('Aoki')
