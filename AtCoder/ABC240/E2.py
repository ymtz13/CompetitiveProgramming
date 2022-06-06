from sys import setrecursionlimit

setrecursionlimit(1000000)

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


def dfs(i, p, cnt=1):
  L = INF
  R = -1

  for e in E[i]:
    if e == p: continue

    l, r, cnt = dfs(e, i, cnt)
    L = min(L, l)
    R = max(R, r)

  if L == INF:
    L = R = cnt
    cnt += 1

  ansL[i] = L
  ansR[i] = R
  return (L, R, cnt)


dfs(0, None)

for l, r in zip(ansL, ansR):
  print(l, r)
