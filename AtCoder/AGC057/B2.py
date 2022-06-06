N, X = map(int, input().split())

A = list(map(int, input().split()))
M = max(A)

B = []
for a in A:
  n = 0
  b = a
  while a << n <= M * 2:
    al = a << n
    ar = al - X + (X << n)

    p = al if al > M else ar if ar < M else M

    if abs(p - M) < abs(b - M): b = p

    n += 1

  B.append(b)

D = max(B) - min(B)

if D + 1 <= X:
  print(0)
else:
  print(D)
