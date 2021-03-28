A, B, W = map(int, input().split())
W *= 1000

nmin = nmax = None
for n in range(1, 2000000):
  ma = A*n
  mb = B*n
  if ma<=W and W<=mb:
    if nmin is None: nmin = n
    nmax = n

if nmin is None:
  print('UNSATISFIABLE')
else:
  print(nmin, nmax)
