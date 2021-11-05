from sys import setrecursionlimit

setrecursionlimit(1000000)

from collections import deque

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
  A, B, C = map(int, input().split())
  E[A - 1].append((B - 1, C))
  E[B - 1].append((A - 1, C))

D = list(map(int, input().split()))

queue = deque([(0, None)])
V = []
P = [None] * N
while queue:
  q, p = queue.popleft()
  V.append(q)
  P[q] = p

  for e, _ in E[q]:
    if e != p: queue.append((e, q))

M = [None] * N
for q in reversed(V):
  m = D[q]
  for e, cost in E[q]:
    if e != P[q]: m = max(m, M[e] + cost)
  M[q] = m

ans = [None] * N


def dfs(i=0, maxBack=0):
  X = []
  for e, cost in E[i]:
    if e != P[i]: X.append(M[e] + cost)

  maxL = [0]
  for x in X:
    maxL.append(max(maxL[-1], x))

  maxR = [0]
  for x in reversed(X):
    maxR.append(max(maxR[-1], x))

  ans[i] = max(maxL[-1], maxBack)

  L = len(X)
  #print('i = {}, L = {}, maxBack={}, maxL = {}, maxR = {}'.format(i, L, maxBack, maxL, maxR))

  n = 0
  for e, cost in E[i]:
    if e == P[i]: continue
    #print(maxL[n], maxR[L - n - 1], maxBack, D[i])
    dfs(e, max(maxL[n], maxR[L - n - 1], maxBack, D[i]) + cost)
    n += 1


dfs()

for a in ans:
  print(a)
