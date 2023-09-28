from collections import deque

mod = 998244353

Q, K = map(int, input().split())
Queries = [input().split() for _ in range(Q)]

dp = [0] * (K + 1)
dp[0] = 1
Ans = []

for t, d in Queries:
  d = int(d)

  dp_next = dp[:]
  if t == '+':
    for i in range(d, K + 1):
      dp_next[i] += dp[i - d]
      dp_next[i] %= mod
  else:
    m = [0] * (K + 1)
    for i in range(d, K + 1):
      v = dp[i - d] - m[i - d]
      dp_next[i] -= v
      m[i] = v
      dp_next[i] %= mod

  dp = dp_next

  Ans.append(dp[-1])

for a in Ans:
  print(a)
