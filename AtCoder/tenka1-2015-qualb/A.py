A = [None] * 30
A[0] = A[1] = 100
A[2] = 200
for i in range(3, 30):
  A[i] = sum(A[i - 3:i])

print(A[19])
