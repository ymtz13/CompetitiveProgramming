from decimal import *
getcontext().prec = 100

F = [Decimal(1)]
for i in range(1, 100):
  F.append(F[-1] * i)


def P(n, m, p, q):
  t1 = F[n - 1] / F[n - 1 - p]
  t2 = F[m - n] / F[m - n - q]
  t3 = F[p + q] / F[p] / F[q]
  t4 = F[m - p - q - 1] / F[m]
  return t1 * t2 * t3 * t4


memo = {}
def dfs(n, m):
  if n == 0: return 0
  if m == 0: return 0

  key = (n, m)
  if key in memo: return memo[key]

  retval = 0
  for p in range(n):
    for q in range(m - n + 1):
      k = (p + q) * 2 + 1 + p + dfs(n - p - 1, m - p - q - 1)
      prob = P(n, m, p, q)
      retval += k * prob
      #print(n, m, p, q, prob, k)

  #print('dfs({}, {}) = {}'.format(n, m, retval))
  memo[key] = retval
  return retval

n, m = map(int, input().split())
print(dfs(n, m))
exit()


S = input()
K = input()
ans0 = 0
for i, c in enumerate(S):
  if c in K or S[:i]:
    ans0 += 1

n0 = len(S) - ans0
m0 = 36 - len(K)

ans = ans0 + dfs(n0, m0)
print(ans)
