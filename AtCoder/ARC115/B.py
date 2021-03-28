import numpy as np

N = int(input())
C = np.empty((N, N), int)
for i in range(N):
  C[i] = np.array(list(map(int, input().split())))

A = C[:, 0].copy()
B = C[0] - A[0]
D = A.reshape(-1, 1) + B

minB = np.min(B)
B -= minB
A += minB

diff = np.abs(C - D)
if np.max(np.abs(C - D)) > 0 or np.min(A) < 0:
  print('No')
else:
  print('Yes')
  print(' '.join(map(str, A)))
  print(' '.join(map(str, B)))
