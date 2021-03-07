L = int(input())
B = [int(input()) for _ in range(L)]

A = [0]*L
for i in range(1, L):
  A[i] = A[i-1] ^ B[i-1]

if A[0]^A[L-1] == B[L-1]:
  for a in A: print(a)
else:
  print(-1)