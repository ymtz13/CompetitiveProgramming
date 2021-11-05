N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

B = [[False]*N for _ in range(N)]
M = int(input())
for _ in range(M):
  X, Y = map(int, input().split())
  B[X-1][Y-1] = True
  B[Y-1][X-1] = True

INF = 10**10
used = [False]*N

def dfs(i, s, last):
  if i==N: return s

  ret = []
  for x in range(N):
    if used[x]: continue
    if last is not None and B[last][x]: continue

    used[x] = True
    ret.append(dfs(i+1, s+A[x][i], x))
    used[x] = False

  return min(ret) if len(ret) else INF


ans = dfs(0, 0, None)
print(ans if ans<INF else -1)
