N, X = map(int, input().split())
S = sorted(list(map(int, input().split())), reverse=True)

mod = 10**9 + 7

dp = [0] * 100010
dp[X] = 1
for n, s in enumerate(S):
  r = N - n - 1
  dp_next = [v * r % mod for v in dp]

  for i, v in enumerate(dp):
    dp_next[i % s] += v

  dp = dp_next

ans = 0
for i, v in enumerate(dp):
  ans += i * v
  ans %= mod

print(ans)
