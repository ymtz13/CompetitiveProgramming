T = int(input())

for _ in range(T):
  N, A, B, C, D = map(int, input().split())
  memo = {}

  def dfs(n):
    if n == 1: return D
    if n == 0: exit()
    if n in memo: return memo[n]

    retval = n * D
    for x, v in zip([2, 3, 5], [A, B, C]):
      n0 = n - n % x
      if n0 > 0:
        retval = min(retval, dfs(n0 // x) + abs(n - n0) * D + v)

      if n != n0:
        n1 = n0 + x
        retval = min(retval, dfs(n1 // x) + abs(n - n1) * D + v)

    memo[n] = retval
    return retval

  print(dfs(N))
