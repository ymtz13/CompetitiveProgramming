mod = 998244353

N, M = map(int, input().split())

C = [0] * 70
m = M
for i in range(1, 70):
  m >>= 1
  if m == 0:
    C[i] = M + 1 - (1 << (i - 1))
    break

  C[i] = (1 << i) - (1 << (i - 1))

dp = [0] * 70
dp[0] = 1

for _ in range(N):
  S = [0]
  for v in dp:
    S.append((S[-1] + v) % mod)

  dp_next = [0] * 70
  for i in range(1, 70):
    dp_next[i] = S[i] * C[i] % mod

  dp = dp_next

  if max(dp) == 0:
    break

ans = 0
for a in dp:
  ans += a
  ans %= mod

print(ans)
