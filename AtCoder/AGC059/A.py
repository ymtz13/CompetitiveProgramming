from collections import defaultdict

D = {'A': 0, 'B': 1, 'C': 2}

N, Q = map(int, input().split())
S = [D[c] for c in input()]

C = [[0] * (N + 1) for _ in range(3)]
count = [0, 0, 0]

for i, c in enumerate(S):
  count[c] += 1
  for p, q in zip(C, count):
    p[i + 1] = q

X = [[None] * N for _ in range(3)]
begin = [0, 0, 0]
for i, c in enumerate(S):
  print(i, c, begin)
  x = X[c]
  for j in range(begin[c], i):
    x[j] = i
  begin[c] = i + 1

for c in range(3):
  x = X[c]
  for j in range(begin[c], N):
    x[j] = N

for x in X:
  print(x)

ans = []
for _ in range(Q):
  L, R = map(int, input().split())

  s = {c[R] - c[L - 1] for c in C}

  if s == {R - L + 1, 0}:
    ans.append(0)
    continue

  if 0 in s:
    ans.append(1)
    continue

  a = N + 10
  for k in range(3):
    x = X[k]
    x1 = X[(k + 1) % 3]
    x2 = X[(k + 2) % 3]

    r = 0
    p = L - 1
    while p < R:
      if x[p] is not None:
        p = x[p]
      else:
        p = max(x1[p], x2[p])
        r += 1

    a = min(a, r)

  ans.append(a + 1)

for a in ans:
  print(a)
