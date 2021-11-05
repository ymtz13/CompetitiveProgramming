from bisect import bisect
INF = 10**10

N = int(input())
A = sorted(list(map(int, input().split())))
Q = int(input())

for _ in range(Q):
  B = int(input())
  i = bisect(A, B)

  L = B - A[i-1] if i>0 else INF
  R = A[i] - B if i<len(A) else INF
  print(min(L, R))
