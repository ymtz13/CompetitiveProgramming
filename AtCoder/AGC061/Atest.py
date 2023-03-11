def s(L, R):
  if L + 1 == R:
    A[L], A[R] = A[R], A[L]
    return

  s(L, R - 1)
  s(L + 1, R)


for N in range(2, 20):
  A = list(range(N + 1))
  s(1, N)

  print('{: d}'.format(N), A[1:])
