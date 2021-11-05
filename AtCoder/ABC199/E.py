N, M = map(int, input().split())
Conds = [[] for _ in range(N)]
for _ in range(M):
  X, Y, Z = map(int, input().split())
  Conds[X-1].append((Y, Z))

def check(i, Used):
  S = [0]
  for x in range(N):
    v = (Used>>x) & 1
    S.append(S[-1] + v)

  for Y, Z in Conds[i]:
    if S[Y]>Z: return False

  return True

memo = [None]*(10**8)

def dfs(i, Used):
  if i==N: return 1
  if memo[Used*20+i] is not None: return memo[Used*20+i]

  retval = 0
  for x in range(N):
    b = 1<<x
    if Used & b: continue

    Used |= b
    if check(i, Used): retval += dfs(i+1, Used)
    Used -= b
  
  memo[Used*20+i] = retval
  return retval

print(dfs(0, 0))
