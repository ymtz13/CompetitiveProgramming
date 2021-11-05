from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A - 1].append(B - 1)

for s in range(N):
  C = [None] * N
  queue = deque([(s, None)])
  t = None
  while queue:
    q, c = queue.popleft()
    if C[q] is not None: continue
    C[q] = c

    if q == s and c is not None:
      t = q
      break

    for e in E[q]:
      queue.append((e, q))

  if t is None:
    continue

  #print(s, C)
  L = []
  q = t
  while True:
    L.append(q)
    q = C[q]
    if q == t: break

  #print(s + 1, [l + 1 for l in L[::-1]])

  L = L[::-1]
  X = [-1] * N
  D = [-1] * N
  for d, l in enumerate(L):
    X[l] = 0
    D[l] = d

  ans = []
  q = L[0]
  while X[q] == 0:
    X[q] = 1
    ans.append(q)

    maxd = -1
    for e in E[q]:
      if X[e] == -1: continue
      dd = (D[e] - D[q]) % len(L)
      if dd > maxd and (D[e] > D[q] or X[e] == 1):
        maxd = dd
        n = e

    q = n
  
  for i, a in enumerate(ans):
    if a==q:
      ans = ans[i:]
      break

  print(len(ans))
  for a in ans:
    print(a + 1)

  exit()

print(-1)