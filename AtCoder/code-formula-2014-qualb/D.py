N = int(input())
A = [0] * 60
for i in range(N):
  A[i] = int(input())

mod = 10**9 + 7

memo = {}


def dfs(i, co):
  if i == 60: return 1

  key = (i, co)
  if key in memo: return memo[key]

  v = A[i] + co
  q = v // 10
  r = v % 10

  retval = (r + 1) * dfs(i + 1, q) % mod
  if q > 0:
    retval += (9 - r) * dfs(i + 1, q - 1) % mod
  retval %= mod

  memo[key] = retval
  return retval


ans = dfs(0, 0) - 1
ans %= mod

print(ans)
