from sys import setrecursionlimit

setrecursionlimit(100000000)

X = 1000000

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  u, v = map(int, input().split())
  E[u - 1].append(v - 1)
  E[v - 1].append(u - 1)

ans = 0
V = [False] * N


def dfs(i):
  global ans

  ans += 1

  if ans >= X:
    print(X)
    exit()

  V[i] = True
  for e in E[i]:
    if V[e]: continue
    dfs(e)
  V[i] = False


dfs(0)

print(ans)
