import numpy as np

R = [[1 if j <= i else 0 for j in range(16)] for i in range(16)]
nR = np.array(R)
nR2 = np.dot(nR, nR)
nR4 = np.dot(nR2, nR2)
nR8 = np.dot(nR4, nR4)
nR16 = np.dot(nR8, nR8)

print(nR2 % 2)
print(nR4 % 2)
print(nR8 % 2)
print(nR16 % 2)

nR12 = np.dot(nR4, nR8)
print(nR12 % 2)

NR = [nR, nR2, nR4, nR8, nR16]
for i in range(16):
  m = np.eye(16, dtype=int)
  for b in range(5):
    if i & (1 << b):
      print(b, 1<<b)
      m = np.dot(m, NR[b]) % 2
  print('---------', i)
  print(m)
  print()

N, M = map(int, input().split())
A = list(map(int, input().split()))
