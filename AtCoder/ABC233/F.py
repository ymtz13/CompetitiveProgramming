from collections import deque

N = int(input())
P = list(map(int, input().split()))
P = [p - 1 for p in P]
L = [None] * N
for i, p in enumerate(P):
  L[p] = i

M = int(input())
E = [[] for _ in range(N)]
C = [[None] * N for _ in range(N)]
for c in range(1, M + 1):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  E[a].append(b)
  E[b].append(a)

  C[a][b] = C[b][a] = c

T = [[] for _ in range(N)]

ans = []

visited = [False] * N
completed = [False] * N
for st in range(N):
  if visited[st]: continue
  order = []
  queue = deque([(st, None)])

  while queue:
    q, f = queue.popleft()
    if visited[q]: continue
    visited[q] = True
    order.append(q)
    if f is not None:
      T[q].append(f)
      T[f].append(q)

    for e in E[q]:
      queue.append((e, q))

  #print(order)
  #print(T)

  for t in reversed(order):
    queue = deque([(t, None)])
    come_from = [None] * N
    while queue:
      q, f = queue.popleft()
      if completed[q]: continue
      come_from[q] = f

      for e in T[q]:
        if e != f: queue.append((e, q))

    #print(t, come_from)

    g = L[t]
    if g == t: continue

    if come_from[g] is None:
      print(-1)
      exit()

    #print('swap {} and {}'.format(t, g))

    while g != t:
      c = come_from[g]

      # swap P[g] and P[c]
      pg = P[g]
      pc = P[c]
      L[pg] = c
      L[pc] = g
      P[g] = pc
      P[c] = pg
      ans.append(C[g][c])

      g = c

    #print('P = ', P)

print(len(ans))
print(' '.join(map(str, ans)))
