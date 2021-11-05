N, Q = map(int, input().split())
Next = [None] * (N + 1)
Prev = [None] * (N + 1)
ans = []

for _ in range(Q):
  query = tuple(map(int, input().split()))
  t = query[0]

  if t == 1:
    x, y = query[1:]
    Next[x] = y
    Prev[y] = x

  if t == 2:
    x, y = query[1:]
    Next[x] = None
    Prev[y] = None

  if t == 3:
    x = query[1]
    while Prev[x] is not None:
      x = Prev[x]

    a = []
    while x is not None:
      a.append(x)
      x = Next[x]

    ans.append(a)

for a in ans:
  print(len(a), ' '.join(map(str, a)))