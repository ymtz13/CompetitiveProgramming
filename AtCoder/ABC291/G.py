import cmath

pi = cmath.pi
exp = cmath.exp

M = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

N = 2**(M - 1).bit_length()

print(M, N)


def make_exp_t(N, base):
  exp_t = {0: 1}
  temp = N
  while temp:
    exp_t[temp] = exp(base / temp)
    temp >>= 1
  return exp_t


fft_exp_t = make_exp_t(N, -2j * pi)
ifft_exp_t = make_exp_t(N, 2j * pi)


def fft_dfs(f, s, N, st, exp_t):
  if N == 2:
    a = f[s]
    b = f[s + st]
    return [a + b, a - b]
  N2 = N // 2
  st2 = st * 2
  F0 = fft_dfs(f, s, N2, st2, exp_t)
  F1 = fft_dfs(f, s + st, N2, st2, exp_t)
  w = exp_t[N]
  wk = 1.0
  for k in range(N2):
    U = F0[k]
    V = wk * F1[k]
    F0[k] = U + V
    F1[k] = U - V
    wk *= w
  F0.extend(F1)
  return F0


def fft(f, N):
  if N == 1:
    return f
  return fft_dfs(f, 0, N, 1, fft_exp_t)


def ifft(F, N):
  if N == 1:
    return F
  f = fft_dfs(F, 0, N, 1, ifft_exp_t)
  for i in range(N):
    f[i] /= N
  return f


V = [0] * M

AA = A[::-1]
BB = B[:]

for i in range(5):
  x = 1 << i
  a = [(1 - ((a >> i) & 1)) for a in AA]
  b = [(1 - ((b >> i) & 1)) for b in BB]
  print(x, a, b)

  a += [0] * (N - M)
  b += [0] * (N - M)

  A = fft(a, N)
  B = fft(b, N)
  AB = [a * b for a, b in zip(A, B)]
  ab = ifft(AB, N)
  ab = [int(c.real + 0.1) for c in ab]

  print(ab)

  for i, v in enumerate(ab[M:]):
    ab[i] += v

  VV = [M - c for c in ab[:M]]
  print(ab[:M], VV)

  for i in range(M):
    V[i] += (M - ab[i]) * x

print(V)

print(max(V))
