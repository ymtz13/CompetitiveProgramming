N = int(input())
A = tuple(map(int, input().split()))
INF = 10**20

def dfs(i, L, OR):
  if i==N:
    if L: return INF
    retval = 0
    for v in OR: retval ^= v
    return retval
  
  v = A[i]
  for x in L: v |= x

  return min(
    dfs(i+1, L[:]+[A[i]], OR),
    dfs(i+1, [], OR[:] + [v])
  )

print(dfs(0, [], []))
