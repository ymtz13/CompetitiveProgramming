from collections import deque

INF = 1 << 20

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
  u, v = map(int, input().split())
  E[u - 1].append(v - 1)
  E[v - 1].append(u - 1)

cnt = 1
ansL = [None] * N
ansR = [None] * N

queue = deque([(0, None)])
parent = [None] * N
D = []
while queue:
  q, p = queue.pop()
  parent[q] = p

  child = 0
  for e in E[q]:
    if e == p: continue
    queue.append((e, q))
    child += 1

  if child == 0:
    ansL[q] = ansR[q] = cnt
    cnt += 1

  else:
    D.append(q)

for d in D[::-1]:
  L = INF
  R = -1

  for e in E[d]:
    if e == parent[d]: continue
    L = min(L, ansL[e])
    R = max(R, ansR[e])

  ansL[d] = L
  ansR[d] = R

for l, r in zip(ansL, ansR):
  print(l, r)
