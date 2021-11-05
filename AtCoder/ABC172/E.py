N, M = map(int, input().split())

mod = 10**9 + 7
K = 1 << 20
F = [1] * K
for p in range(1, K):
  F[p] = F[p - 1] * p % mod

Finv = [None] * K
Finv[K - 1] = pow(F[K - 1], mod - 2, mod)
for p in range(K - 2, -1, -1):
  Finv[p] = Finv[p + 1] * (p + 1) % mod

ans = 0
for i in range(N + 1):
  sign = (-1)**i
  comb = F[N] * Finv[N - i] * Finv[i] % mod
  coef = F[M - i] * Finv[M - N] % mod

  ans = (ans + sign * comb * coef) % mod

ans = (ans * F[M] * Finv[M - N] % mod)

print(ans)

# |S[]| - |S[1] U S[2] U ... U S[N]|

# = + (-1)^0 |S[]|
#   + (-1)^1 |S[1]| + |S[2]| + ... + |S[N]|
#   + (-1)^2 |S[1,2]| + |S[1,3]| + ... + |S[N-1, N]|
#   + (-1)^3 |S[1,2,3]| + |S[1,2,4]| + ... + |S[N-2,N-1, N]|
#   ...
#   + (-1)^N |S[1,2,...,N]|

# = + (-1)^0 Comb(N, 0) |S[]|
#   + (-1)^1 Comb(N, 1) |S[1]|
#   + (-1)^2 Comb(N, 2) |S[1,2]|
#   + (-1)^3 Comb(N, 3) |S[1,2,3]|
#   ...
#   + (-1)^N Comb(N, N) |S[1,2,...,N]|

# = + (-1)^0 Comb(N, 0) (M-0)! / (M-N)!
#   + (-1)^1 Comb(N, 1) (M-1)! / (M-N)!
#   + (-1)^2 Comb(N, 2) (M-2)! / (M-N)!
#   + (-1)^3 Comb(N, 3) (M-3)! / (M-N)!
#   ...
#   + (-1)^N Comb(N, N) (M-N)! / (M-N)!