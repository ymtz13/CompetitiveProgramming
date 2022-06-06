N = int(input())

A = [1]
for _ in range(N):
  print(' '.join(map(str, A)))

  B = []
  for a, b in zip([0] + A, A + [0]):
    B.append(a + b)
  A = B
