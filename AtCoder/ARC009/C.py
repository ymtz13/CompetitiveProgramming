N, K = map(int, input().split())
mod = 1777777777

# | S(1) U S(2) U S(3) U ... U S(N) |
# = + |S(1)| + |S(2)| + |S(3)| + ... + |S(N)|
#   - |S(1,2)| + |S(1,3)| + ... + |S(N-1, N)|
#   + |S(1,2,3)| + ... + |S(N-2, N-1, N)|
#   ...
#   + (-1)^(N-1) |S(1,2,3,...,N)|

# = + comb(K, 1) (K-1)!
#   - comb(K, 2) (K-2)!
#   + comb(K, 3) (K-3)!
#   ...
#   + (-1)^(N-1) comb(K, K) (K-K)!

# = + K! / 1!
#   - K! / 2!
#   + K! / 3!
#   ...
#   + (-1)^(N-1) K! / K!

# = K! f(K)

# ans = comb(N, K) * (K! - K! f(K))
#     = N! / (N-K!) * (1 - f(K))

x = 1
for n in range(N, N - K, -1):
  x *= n
  x %= mod

F = [1]
for i in range(1, K + 1):
  F.append(F[-1] * i % mod)

Finv = [None] * (K + 1)
Finv[-1] = pow(F[-1], mod - 2, mod)
for i in range(K - 1, -1, -1):
  Finv[i] = Finv[i + 1] * (i + 1) % mod

y = 1
for i in range(1, K + 1):
  s = 1 - i % 2 * 2
  y += s * Finv[i]
  y %= mod

print(x * y % mod)
