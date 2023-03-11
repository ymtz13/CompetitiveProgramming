mod = 998244353


def inv(x):
  return pow(x, mod - 2, mod)


N = map(int, input().split())
A = list(map(int, input().split()))[::-1]

E = [0]
S = [0, 0]
for i, a in enumerate(A):
  p0 = inv(a + 1)
  e0 = p0 * inv(1 - p0) % mod

  s = S[-1] - S[-1 - a]
  e = 1 + e0 + s * inv(a) % mod
  e %= mod

  E.append(e)
  S.append((S[-1] + e) % mod)

print(E[-1])
