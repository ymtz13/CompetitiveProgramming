N, M = map(int, input().split())
N2 = 2 * N

mod = 998244353

memo = {}

P = [[False] * N2 for _ in range(N2)]
for _ in range(M):
  A, B = map(int, input().split())
  P[A - 1][B - 1] = P[B - 1][A - 1] = True

F = [1]
for p in range(1, 300):
  F.append(F[-1] * p % mod)

Finv = [pow(f, mod - 2, mod) for f in F]


def solve(bgn, end):
  if end - bgn == 1: return 1 if P[bgn][end] else 0

  key = bgn * 1000 + end
  if key in memo: return memo[key]

  retval = 0
  for mid in range(bgn + 1, end, 2):
    if not P[bgn][mid]: continue

    lenL = (mid - bgn + 1) // 2
    lenR = (end - mid) // 2
    coeff = F[lenL + lenR] * Finv[lenL] * Finv[lenR]

    solveL = solve(bgn + 1, mid - 1) if mid > bgn+1 else 1
    solveR = solve(mid + 1, end)

    retval += coeff * solveL * solveR % mod
    retval %= mod

  if P[bgn][end]:
    retval += solve(bgn + 1, end - 1)

  retval %= mod
  memo[key] = retval
  return retval


print(solve(0, N2 - 1))
