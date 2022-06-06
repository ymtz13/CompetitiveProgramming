from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
B = [[] for _ in range(N + 1)]
for i, a in enumerate(A, 1):
  B[a].append(i)

Q = int(input())
ans = []
for _ in range(Q):
  L, R, X = map(int, input().split())
  iL = bisect_left(B[X], L)
  iR = bisect_left(B[X], R + 1)
  ans.append(iR - iL)

for a in ans:
  print(a)