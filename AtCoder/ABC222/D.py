N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = 3010
dp = [0] * M
dp[0] = 1

mod = 998244353

for a, b in zip(A, B):
  dp_next = [0] * M
  s = 0
  for c, v in enumerate(dp):
    s = (s + v) % mod
    if c >= a and c <= b: dp_next[c] = s

  dp = dp_next

ans = 0
for v in dp:
  ans += v
  ans %= mod

print(ans)

