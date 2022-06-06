from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
Einv = [[] for _ in range(N)]

for _ in range(M):
  U, V = map(int, input().split())
  E[U - 1].append(V - 1)
  Einv[V - 1].append(U - 1)

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
    #print(stack)

#print(C)

R = [False] * N
SCCs = []
for _, v in sorted(C, reverse=True):
  if R[v]: continue

  stack = deque([v])
  SCC = []

  while stack:
    v = stack.pop()
    if R[v]: continue
    R[v] = True
    SCC.append(v)

    for e in Einv[v]:
      stack.append(e)

  #print(SCC)
  SCCs.append(SCC)

OK = [None] * N
for SCC in SCCs:
  if len(SCC) == 1: continue
  for v in SCC:
    OK[v] = True

for i in range(N):
  if not OK[i]: continue

  stack = deque([i])
  while stack:
    v = stack.pop()
    OK[v] = True

    for e in Einv[v]:
      if not OK[e]: stack.append(e)

#print(OK)
print(OK.count(True))
