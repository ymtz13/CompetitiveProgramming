from collections import deque

def scc(E):
  N = len(E)
  Einv = [[] for _ in range(N)]
  for u, edges in enumerate(E):
    for e in edges:
      Einv[e].append(u)

  cnt = 0
  C = [None] * N
  R = [False] * N

  for st in range(N):
    if R[st]: continue
    stack = deque([(0, st)])

    while stack:
      t, v = stack.pop()
      if t == 0 and R[v]: continue
      R[v] = True

      if t == 0:
        stack.append((1, v))
        for e in E[v]:
          stack.append((0, e))

      if t == 1:
        C[v] = (cnt, v)
        cnt += 1

  sccs = []
  R = [False] * N
  for _, v in sorted(C, reverse=True):
    if R[v]: continue

    stack = deque([v])
    scc = []

    while stack:
      v = stack.pop()
      if R[v]: continue
      R[v] = True
      scc.append(v)

      for e in Einv[v]:
        stack.append(e)

    sccs.append(scc)
  
  return sccs

E = [
  [1], # 0
  [2], # 1
  [0, 3], # 2
  [4], # 3
  [3, 5, 6], # 4
  [], # 5
  [], # 6  
]

print(scc(E))

