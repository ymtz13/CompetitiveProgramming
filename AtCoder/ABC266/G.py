mod = 998244353

F = [1]
for i in range(1, 4000010):
  F.append(F[-1] * i % mod)


def inv(X):
  return pow(X, mod - 2, mod)


def comb(A, B):
  return F[A] * inv(F[B]) * inv(F[A - B]) % mod


R, G, B, K = map(int, input().split())


def f(R, G, B, K):
  if K > min(R, G): return 0

  R -= K
  G -= K

  retval = F[R + G + B + K]
  for X in (R, G, B, K):
    retval *= inv(F[X])
    retval %= mod

  return retval


ans = f(R, G, B, K)
for X in range(1, min(R, G) - K + 1):
  P = comb(K + X, X)
  f -= f(R, G, B, K + 1) * P

print(ans)
