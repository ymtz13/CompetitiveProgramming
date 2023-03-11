mod = 998244353

N, K = map(int, input().split())
PQ = [(int(p), int(q)) for p, q in zip(input().split(), input().split())]
PQ.sort()

M = 320
M2 = M * M
memo = [None] * M * M * M


def solve(i, k, qbound):
  key = i * M2 + k * M + qbound
  if memo[key] is not None: return memo[key]

  if k == 0: return 1
  if i == N: return 0

  _, Q = PQ[i]
  retval = solve(i + 1, k, min(qbound, Q))
  if Q < qbound:
    retval += solve(i + 1, k - 1, qbound)
    retval %= mod

  memo[key] = retval
  return retval


ans = solve(0, K, N + 10)
print(ans)
