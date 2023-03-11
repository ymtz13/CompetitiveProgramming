from collections import defaultdict

N = int(input())
D = {}
E = {}

for _ in range(N):
  S, T = input().split()

  if S not in D: D[S] = len(D)
  if T not in D: D[T] = len(D)
  iS = D[S]
  iT = D[T]

  E[iS] = iT

M = len(D)
visited = [False] * M

for s in range(M):
  if visited[s]: continue

  Q = set()
  while s in E:
    visited[s] = True
    Q.add(s)
    s = E[s]
    if s in Q:
      print('No')
      exit()

print('Yes')
