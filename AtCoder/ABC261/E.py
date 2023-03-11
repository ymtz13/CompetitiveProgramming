N, C = map(int, input().split())
X = [(C >> i) & 1 for i in range(40)]

O = [None] * 40
ans = []
for _ in range(N):
  T, A = map(int, input().split())
  A = [(A >> i) & 1 for i in range(40)]

  if T == 1:
    for i, a in enumerate(A):
      if a == 0: O[i] = 0

  if T == 2:
    for i, a in enumerate(A):
      if a == 1: O[i] = 1

  if T == 3:
    for i, a in enumerate(A):
      if a == 0: continue
      if O[i] == 0: O[i] = 1
      elif O[i] == 1: O[i] = 0
      elif O[i] == -1: O[i] = None
      elif O[i] is None: O[i] = -1

  for i, o in enumerate(O):
    if o == 0: X[i] = 0
    if o == 1: X[i] = 1
    if o == -1: X[i] = 1 - X[i]

  a = 0
  for i, x in enumerate(X):
    if x: a += 1 << i
  ans.append(a)

for a in ans:
  print(a)
