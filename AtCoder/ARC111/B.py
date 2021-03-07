from collections import deque, defaultdict

N = int(input())
M = 400000
AB = [tuple(map(int, input().split())) for _ in range(N)]
E = [defaultdict(int) for _ in range(M)]
C = set()
for a, b in AB:
  E[a-1][b-1] += 1
  E[b-1][a-1] += 1
  C.add(a-1)
  C.add(b-1)

V = [False]*M
nTree = 0
for st in C:
  if V[st]: continue

  isTree = True
  queue = deque([st])
  while queue:
    q = queue.popleft()
    if V[q]:
      isTree = False
      continue
    V[q] = True
    #print(q)

    for e, c in E[q].items():
      if c==0: continue
      if c>1: isTree = False
      E[q][e] -= 1
      E[e][q] -= 1
      queue.append(e)

  if isTree: nTree += 1
  #print(st, isTree)

print(len(C) - nTree)
