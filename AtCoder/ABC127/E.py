H, W, K = map(int, input().split())
mod = 10**9 + 7
ans = 0

F = [1]
for i in range(1, H * W + 10):
  F.append(F[-1] * i % mod)


def comb(n, k):
  return F[n] * pow(F[k], mod - 2, mod) * pow(F[n - k], mod - 2, mod) % mod


C = comb(H * W - 2, K - 2)

for h in range(1, H):
  ans += h * (H - h) * W * W * C
  ans %= mod

for w in range(1, W):
  ans += w * (W - w) * H * H * C
  ans %= mod

print(ans)
