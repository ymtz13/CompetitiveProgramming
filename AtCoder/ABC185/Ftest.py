from random import randint

N = 300000
Q = 300000
print(N, Q)

A = [randint(0, 2**30-1) for _ in range(N)]
print(' '.join(map(str, A)))

for q in range(Q):
  T = randint(1, 2)
  if T==1:
    X = randint(1, N)
    Y = randint(0, 2**30-1)
  else:
    X = randint(1, N)
    Y = randint(X, N)
  print(T, X, Y)
