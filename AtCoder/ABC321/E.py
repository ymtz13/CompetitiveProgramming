T = int(input())


def count(N, i, k):
  L = i << k
  R = ((i + 1) << k) - 1

  if N < L:
    return 0
  if N < R:
    return N - L + 1
  return R - L + 1


for _ in range(T):
  N, X, K = map(int, input().split())

  if K > 200:
    print(0)
    continue

  ans = count(N, X, K)
  prev = X
  while X > 1:
    X >>= 1
    lc = X << 1
    rc = lc + 1
    c = lc + rc - prev
    prev = X
    K -= 1
    if K >= 1:
      ans += count(N, c, K - 1)
    if K == 0:
      ans += 1

  print(ans)
