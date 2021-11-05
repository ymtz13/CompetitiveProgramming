K = int(input())
S = len(input())
mod = 1000000007

F = [1]
for p in range(1, K + S + 1):
  F.append(F[-1] * p % mod)


def comb(k, x):
  return F[k] * pow(F[k - x], mod - 2, mod) * pow(F[x], mod - 2, mod) % mod


ans = 0
for x in range(K + 1):
  ans += comb(S + K, x) * pow(25, x, mod)
  ans %= mod

print(ans)
