from sys import setrecursionlimit
setrecursionlimit(100000)

X, Y = map(int, input().split())
if X>=Y:
  print(X-Y)
  exit()

memo = {}
def dfs(Y):
  if Y in memo: return memo[Y]
  if Y==0: return X
  if Y==1: return X-1

  if Y%2==0:
    retval = min(abs(X-Y), dfs(Y//2) + 1)
  else:
    retval = min(abs(X-Y), dfs(Y//2) + 2, dfs(Y//2 + 1) + 2)
  
  memo[Y] = retval
  return retval

print(dfs(Y))
