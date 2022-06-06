from sys import setrecursionlimit

setrecursionlimit(1000000)

N, Q = map(int, input().split())
X = list(map(int, input().split()))
E = [[] for _ in range(N)]
for _ in range(N - 1):
  A, B = map(int, input().split())
  E[A - 1].append(B - 1)
  E[B - 1].append(A - 1)

T = [None] * N


def dfs(i, p):
  t = [X[i]]

  for e in E[i]:
    if e == p: continue
    t.extend(dfs(e, i))

  t = sorted(t, reverse=True)[:20]
  T[i] = t
  return t


dfs(0, None)

for _ in range(Q):
  V, K = map(int, input().split())
  print(T[V - 1][K - 1])
