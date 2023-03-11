import re

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

T = [(i + 1, a, b, a + b) for i, (a, b) in enumerate(zip(A, B))]

ans = []

T.sort(key=lambda x: (x[1] * N - x[0]), reverse=True)
ans.extend(T[:X])
T = T[X:]

T.sort(key=lambda x: (x[2] * N - x[0]), reverse=True)
ans.extend(T[:Y])
T = T[Y:]

T.sort(key=lambda x: (x[3] * N - x[0]), reverse=True)
ans.extend(T[:Z])

ans.sort()
for a in ans:
  print(a[0])
