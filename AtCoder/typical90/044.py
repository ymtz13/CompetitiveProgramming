N, Q = map(int, input().split())
M = 10**6
A = [None]*M + list(map(int, input().split()))

bgn = M-1
for _ in range(Q):
  T, x, y = map(int, input().split())

  if T==1: A[bgn+x], A[bgn+y] = A[bgn+y], A[bgn+x]
  if T==2: A[bgn], A[bgn+N], bgn = A[bgn+N], None, bgn - 1
  if T==3: print(A[bgn+x])
