N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(range(1, N + 1))
C = []

for a in A:
  l = a - 1
  r = a

  bl = B[l]
  br = B[r]

  if bl == 1:
    C.append(br)
  elif br == 1:
    C.append(bl)
  else:
    C.append(1)

  B[l] = br
  B[r] = bl

X = [None] * (N + 1)
for i, b in enumerate(B):
  X[b] = i + 1

for c in C:
  print(X[c])
