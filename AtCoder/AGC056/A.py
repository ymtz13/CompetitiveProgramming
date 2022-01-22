N = int(input())
A = [['.'] * N for _ in range(N)]
j = 0
I = []
for i in range(N):
  for _ in range(3):
    A[i][j] = '#'
    j += 1
    if j == N:
      j = 0
      I.append(i)

if N % 3 > 0:
  i1, i2 = I[:2]
  A[0], A[i1 - 1] = A[i1 - 1], A[0]
  A[-1], A[i2 + 1] = A[i2 + 1], A[-1]

for row in A:
  print(''.join(row))
