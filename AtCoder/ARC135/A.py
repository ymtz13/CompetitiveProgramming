X = int(input())
mod = 998244353

memo = {0: 0, 1: 1}


def dfs(x):
  if x <= 4: return x
  if x in memo: return memo[x]

  x0 = x // 2
  x1 = (x + 1) // 2

  retval = dfs(x0) * dfs(x1) % mod
  memo[x] = retval
  return retval


print(dfs(X))
