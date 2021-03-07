N, K = map(int, input().split())
T = [tuple(map(int, input().split())) for _ in range(N)]

P = [0]*N
used = [False]*N

def dfs(i, s):
  if i==N:
    return 1 if s+T[0][P[-1]]==K else 0

  retval = 0
  for n in range(1, N):
    if used[n]: continue
    used[n] = True
    P[i] = n
    ss = s + T[n][P[i-1]]
    retval += dfs(i+1, ss)
    used[n] = False
  
  return retval

print(dfs(1, 0))