from sys import setrecursionlimit

setrecursionlimit(10**8)

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
  a, b = map(int, input().split())
  E[a - 1].append(b - 1)
  E[b - 1].append(a - 1)

memo = {}
mod = 10**9 + 7

F = [1]
for i in range(1, 1 << 18):
  F.append(F[-1] * i % mod)

Finv = [None] * len(F)
Finv[-1] = pow(F[-1], mod - 2, mod)

for i in range(len(F) - 1, 0, -1):
  Finv[i - 1] = Finv[i] * i % mod

A = [None] * N

Z = 1 << 19


def dfs(i, p):
  key = (i << 20) + p
  if key in memo: return memo[key]

  if A[i] is None:
    s = 0
    t = 1
    for c in E[i]:
      if c == p: continue

      m, x = dfs(c, i)
      s += m
      t *= x * Finv[m]
      t %= mod

    A[i] = (1, t, p) if p != Z else (2, t)

    r = t * F[s] % mod

  else:
    if A[i][0] == 1:
      _, t, c = A[i]
      m, x = dfs(c, i)
      t *= x * Finv[m]
      A[i] = (2, t)

    _, t = A[i]
    if p != Z:
      m, x = dfs(p, i)
      s = N - 1 - m
      r = t * pow(x * Finv[m], mod - 2, mod) * F[s] % mod
    else:
      s = N - 1
      r = t * F[s] % mod

  retval = (s + 1, r)
  memo[key] = retval

  return retval


for i in range(N):
  _, ans = dfs(i, Z)
  print(ans)
