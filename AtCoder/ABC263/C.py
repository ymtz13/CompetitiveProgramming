from collections import deque

N, M = map(int, input().split())

X = []
stack = deque([(0, True)])
while stack:
  v, f = stack.pop()

  if f:
    stack.append((v, False))

    X.append(v)
    if len(X) == N + 1:
      print(' '.join(map(str, X[1:])))
      continue

    for w in range(M, v, -1):
      stack.append((w, True))

  else:
    X.pop()
