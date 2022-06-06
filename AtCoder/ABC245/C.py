N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

X = {A[0], B[0]}
for Y in zip(A[1:], B[1:]):
  X2 = set()
  for x in X:
    for y in Y:
      if abs(x - y) <= K:
        X2.add(y)
  X = X2

print('Yes' if X else 'No')