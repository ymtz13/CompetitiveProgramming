from sys import setrecursionlimit
setrecursionlimit(1000000)

N, M = map(int, input().split())
A = list(map(int, input().split()))
E = [[] for _ in range(N)]
for _ in range(M):
  X, Y = map(int, input().split())
  E[X-1].append(Y-1)

V = [None]*N
INF = 10**10
ans = -INF
def dfs(i):
  global ans

  if V[i] is not None:
    return V[i]

  m = -INF
  for e in E[i]:
    m = max(m, dfs(e))

  ans = max(ans, m - A[i])
  
  retval = max(A[i], m)
  V[i] = retval
  return retval

for i in range(N):
  dfs(i)

print(ans)
