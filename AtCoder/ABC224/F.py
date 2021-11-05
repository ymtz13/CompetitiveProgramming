S = list(map(int, input()))[::-1]
N = len(S)

ans = 0
P = 1
mod = 998244353

for i, d in enumerate(S):
  coeff = d * pow(2, N - i - 1, mod)
  coeff %= mod

  ans += coeff * pow(10, i, mod)
  ans %= mod

  if i > 0:
    ans += coeff * P
    ans %= mod

    P *= 10
    P += pow(2, i, mod)
    P %= mod

print(ans)
