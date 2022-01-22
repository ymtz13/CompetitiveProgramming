R, C = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())

mod = 10**9 + 7

F = [1]
for i in range(1, 20000):
  F.append(F[-1] * i % mod)


def comb(n, k):
  if n < k: return 0
  return F[n] * pow(F[n - k], mod - 2, mod) * pow(F[k], mod - 2, mod) % mod


def f(x, y):
  if x < 0 or y < 0: return 0
  s = x * y
  return comb(s, D) * comb(s - D, L) % mod


ans = 0
ans += f(X, Y)
ans -= 2 * f(X - 1, Y) + 2 * f(X, Y - 1)
ans += 4 * f(X - 1, Y - 1) + f(X - 2, Y) + f(X, Y - 2)
ans -= 2 * f(X - 2, Y - 1) + 2 * f(X - 1, Y - 2)
ans += f(X - 2, Y - 2)

ans *= (R - X + 1) * (C - Y + 1)
ans %= mod

print(ans)
