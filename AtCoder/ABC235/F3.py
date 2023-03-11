mod = 998244353


def toArray(B):
  return [i for i in range(10) if B & (1 << i)]


def toB(C):
  return sum([1 << i for i in C])


def f(N, C):
  # 0 <= x < 10**N
  S = sum(C)
  V = (pow(10, N, mod) - 1) * pow(9, mod - 2, mod) % mod
  X = pow(len(C), N - 1, mod)
  return S * V * X % mod


def g(N, C):
  retval = 0
  for mask in range(1 << len(C)):
    CC = [c for i, c in enumerate(C) if mask & (1 << i)]
    sign = (-1)**(len(C) - len(CC))
    retval += sign * f(N, CC)
    print(CC, sign)
    retval %= mod

  return retval


print(g(3, [1, 2, 3]))
print('-------')

print(f(3, []))
print(f(3, [1]))
print(f(3, [2]))
print(f(3, [1, 2]))
