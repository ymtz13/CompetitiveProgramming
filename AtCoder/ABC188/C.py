N = int(input())
A = list(enumerate(map(int, input().split())))
for i in range(N-1):
  An = []
  for (i1, a1), (i2, a2) in zip(A[0::2], A[1::2]):
    An.append((i1, a1) if a1>a2 else (i2, a2))
  A = An

(i1, a1), (i2, a2) = A
print(i1 + 1 if a1<a2 else i2 + 1)
