def comb(N, K):
  retval = 1.0
  for i in range(K):
    retval = retval * (N - i) / (i + 1)
  return retval


def solve(N, D, X, Y):
  if X % D != 0 or Y % D != 0: return 0
  X, Y = X // D, Y // D
  if (X + Y) % 2 != N % 2: return 0

  S = (N + X + Y) // 2
  T = (N + X - Y) // 2

  Ps = comb(N, S) / 2.0**N
  Pt = comb(N, T) / 2.0**N

  return Ps * Pt


N, D = map(int, input().split())
X, Y = map(int, input().split())

print(solve(N, D, X, Y))
