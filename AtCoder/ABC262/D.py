mod = 998244353

N = int(input())
A = list(map(int, input().split()))

ans = 0
for n in range(1, N + 1):
  m = n + 1
  dp = [0] * m * n
  dp[0] = 1

  for a in A:
    for i in range(n - 1, -1, -1):
      for r in range(n):
        x = (i + 1) * n + (r + a) % n
        dp[x] += dp[i * n + r]
        dp[x] %= mod

  ans += dp[n * n]
  ans %= mod

print(ans)
