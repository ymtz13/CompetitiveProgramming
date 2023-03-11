N = int(input())
A = list(map(int, input().split()))


INF = 1<<60
fmax = -INF
fmin = +INF

FMax = [None]*N
FMin = [None]*N

c = d= 0
for i in range(N-1, -1, -1):
  d += c
  c += A[i]

  FMax[i] = 



