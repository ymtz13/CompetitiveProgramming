N = 100
X = [0] * N
X[1] = 1

for _ in range(300):
  print(''.join(['o' if x else ' ' for x in X]))
  X2 = [0] * N
  for i in range(1, N):
    X2[i] = X[i - 1] ^ X[i]
  X = X2
