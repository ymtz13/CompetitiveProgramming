from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
D = {}

for _ in range(M):
  A, B = map(int, input().split())
  A -= 1
  B -= 1

  E[A].append(B)
  E[B].append(A)

  D[A * N + B] = +1
  D[B * N + A] = -1

# for e in E:
#   if len(e) % 2 == 1:
#     print(-1)
#     exit()

visited = [False] * N
stack = deque([(0, 0, None)])
path = None

# print('dfs')

while stack:
  q, d, par = stack.pop()

  if d == 1:
    if path is not None: path.append(q)
    # print(q + 1, 'Backward')
    continue

  if visited[q]: continue
  visited[q] = True
  # print(q + 1, 'Forward')
  if par is not None: stack.append((par, 1, None))

  outdegree = 0
  for e in E[q]:
    if D[q * N + e] == 1: outdegree += 1

  # print('outdeg[', q + 1, ']=', outdegree)

  if outdegree % 2 == 1:
    if path is None:
      path = [q]

    else:
      qq = q
      # print('flip, path=', path)
      for pp in path[::-1]:
        # print('pp,qq = ', pp, qq)
        D[pp * N + qq] *= -1
        D[qq * N + pp] *= -1
        qq = pp

      # print(path)
      path = None

  elif path is not None:
    path.append(q)

  for e in E[q]:
    if not visited[e]:
      # stack.append((q, 1))
      stack.append((e, 0, q))

  # childs = [e for e in E[q] if not visited[e]]

  # if childs: stack.append((q, 1))
  # for e in childs:
  #   stack.append((e, 0))

# print('path', path)

if path is not None:
  print(-1)
  exit()

for d, v in D.items():
  if v == -1: continue

  A, B = d // N, d % N
  print(A + 1, B + 1)
