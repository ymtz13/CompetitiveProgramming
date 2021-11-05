mod = 998244353
N = int(input())
A = list(map(int, input().split()))

dp = [0] * 10
dp[A[0]] = 1

for a in A[1:]:
  dp_next = [0] * 10
  for d in range(10):
    dp_next[(d + a) % 10] += dp[d]
    dp_next[(d * a) % 10] += dp[d]
  dp = [v % mod for v in dp_next]

for v in dp:
  print(v)
