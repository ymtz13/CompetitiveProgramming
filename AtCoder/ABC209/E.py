from collections import deque

N = int(input())
S = []
D = {}      # D['abc'] == 0
Dinv = []   # Dinv[0]  == 'abc'
Edges = []

SFST = set()

for _ in range(N):
  s = input()
  S.append(s)
  sf = s[:3]
  st = s[-3:]

  sfst = sf + st
  if sfst in SFST: continue
  SFST.add(sfst)

  if sf not in D:
    D[sf] = len(Dinv)
    Dinv.append(sf)
  
  if st not in D:
    D[st] = len(Dinv)
    Dinv.append(st)
  
  isf = D[sf]
  ist = D[st]
  Edges.append((isf, ist))

V = len(Dinv)
E = [[] for _ in range(V)]
Einv = [[] for _ in range(V)]
Deg = [0]*V # 出次数
for isf, ist in Edges:
  E[isf].append(ist)
  Einv[ist].append(isf)
  Deg[isf] += 1

queue = deque([i for i in range(V) if len(E[i]) == 0]) # 出次数0のノード
nodeTypes = [None]*V
#print(queue, [Dinv[q] for q in queue])

while queue:
  q = queue.popleft()

  nodeType = 'L'
  for e in E[q]:
    if nodeTypes[e] == 'L':
      nodeType = 'W'
      break
  nodeTypes[q] = nodeType

  for p in Einv[q]:
    Deg[p] -= 1
    if Deg[p] == 0 or (nodeType == 'L' and nodeTypes[p] is None):
      queue.append(p)
      Deg[p] = 0

for s in S:
  st = s[-3:]
  ist = D[st]

  nodeType = nodeTypes[ist]
  if   nodeType is None:
    print('Draw')
  elif nodeType == 'W':
    print('Aoki')
  else:
    print('Takahashi')

for key, value in D.items():
  print(key, value, nodeTypes[value])
