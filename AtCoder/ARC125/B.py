N = int(input())
mod = 998244353

ans = 0
for d in range(1, N + 1):
  if d * d - 100 > N: break
  u = (N + d * d) // (2 * d)
  l = d
  ans += max(0, u - l + 1)
  ans %= mod

print(ans)
