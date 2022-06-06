mod = 998244353

Finv = [1] + [pow(i, mod - 2, mod) for i in range(1, 210)]


def comb(n, k):
  r = 1
  for i in range(k):
    r *= (n - i) * Finv[i + 1]
    r %= mod
  return r


N, K = map(int, input().split())
A = list(map(int, input().split()))

if A[0] < N:
  print(0)
  exit()

A[0] = A[0] - K - sum(A[1:])

if A[0] < 0:
  print(0)
  exit()

ans = 1
for a in A:
  ans *= comb(a + K - 1, K - 1)
  ans %= mod

print(ans)
