from sys import setrecursionlimit
from collections import deque

setrecursionlimit(1 << 16)

N = int(input())
M = N * 2
E = [[] for _ in range(N)]
for i in range(N - 1):
  u, v = map(int, input().split())
  E[u - 1].append(v - 1)
  E[v - 1].append(u - 1)

P = [None] * N


def dfs(i, p):
  cnt = dist = 0
  for e in E[i]:
    if e == p: continue
    dist += dfs(e, i)
    cnt += C[e]
  dist += cnt
  cnt += 1

  P[i] = p
  C[i] = cnt
  return dist


C = [None] * N
s = dfs(0, -1)

queue = deque([])

def solve(i, p, s):
  if p is not None: s -= C[i] * 2 - N
  ans[i] = s

  for e in E[i]:
    if e == p: continue
    solve(e, i, s)


ans = [None] * N
#solve(0, None, s)
#for a in ans:
#  print(a)