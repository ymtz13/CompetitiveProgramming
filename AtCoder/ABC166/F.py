N, A, B, C = map(int, input().split())
S = [input() for _ in range(N)]
D = {'AB': (0, 1), 'BC': (1, 2), 'AC': (2, 0)}

if A + B + C <= 2:

  path = []
  dp = {(A, B, C): None}

  for n, s in enumerate(S):
    p1, p2 = D[s]

    diff = [0, 0, 0]
    diff[p1] += 1
    diff[p2] -= 1

    dp_next = {}
    for abc in dp:
      t1 = tuple(v + dv for v, dv in zip(abc, diff))
      t2 = tuple(v - dv for v, dv in zip(abc, diff))

      if abc[p2] > 0 and t1 not in dp_next: dp_next[t1] = (p1, p2)
      if abc[p1] > 0 and t2 not in dp_next: dp_next[t2] = (p2, p1)

    dp = dp_next
    path.append(dp)

  if len(path[-1]) > 0:
    print('Yes')

    ans = []
    t = list(path[-1].keys())[0]
    for pp in reversed(path):
      p1, p2 = pp[t]

      diff = [0, 0, 0]
      diff[p1] += 1
      diff[p2] -= 1

      t = tuple(v - dv for v, dv in zip(t, diff))
      ans.append('ABC'[p1])

    for a in ans[::-1]:
      print(a)

  else:
    print('No')

else:

  ans = []
  t = (A, B, C)
  for n, s in enumerate(S):
    p1, p2 = D[s]

    if t[p1] == 0 and t[p2] == 0:
      print('No')
      exit()

    diff = [0, 0, 0]
    diff[p1] += 1
    diff[p2] -= 1
    t1 = tuple(v + dv for v, dv in zip(t, diff))
    t2 = tuple(v - dv for v, dv in zip(t, diff))

    t, p = (t2, p2) if max(t1) == A + B + C or min(t1) < 0 else (t1, p1)
    ans.append('ABC'[p])

  print('Yes')
  for a in ans:
    print(a)
