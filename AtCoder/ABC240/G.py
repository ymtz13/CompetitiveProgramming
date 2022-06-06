mod = 998244353

N, X, Y, Z = map(int, input().split())

M = 200000
F = [1]
for i in range(1, M):
  F.append(F[-1] * i % mod)
Finv = [None] * M
Finv[-1] = pow(F[-1], mod - 2, mod)
for i in range(M - 1, -1, -1):
  Finv[i - 1] = Finv[i] * i % mod


def comb(n, k):
  return F[n] * Finv[k] * Finv[n - k] % mod


ans = 0

for zp in range(N + 1):
  zn = abs(Z - zp)
  if zn < 0: continue

  NN = N - zp - zn
  if NN < 0: continue

  x = X + Y
  y = X - Y

  if NN % 2 != x % 2 or NN % 2 != y % 2:
    continue
  if x > NN or x < -NN or y > NN or y < -NN:
    continue

  xp = (NN + x) // 2
  xn = NN - xp
  yp = (NN + y) // 2
  yn = NN - yp

  print('xx', zp, zn, NN, xp, xn, yp, yn)

  f1 = comb(N, zp) * comb(N - zp, zn)
  f2 = comb(NN, xp) * comb(NN - xp, xn)
  f3 = comb(NN, yp) * comb(NN - yp, yn)
  #f4 = pow(pow(2, NN, mod), mod - 2, mod)
  f4 = 1

  ans += f1 * f2 * f3 * f4 % mod
  ans %= mod

print(ans)
