N = int(input())
A = [2]*(N+1)
A[1] = 1
for i in range(2, N+1):
  a = A[i] + 1
  for j in range(i*2, N+1, i):
    A[j] = max(A[j], a)
  
print(' '.join(map(str, A[1:])))
