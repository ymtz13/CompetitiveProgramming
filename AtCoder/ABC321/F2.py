from collections import deque

mod = 998244353

Q, K = map(int, input().split())
Queries = [tuple(map(int, input().split())) for _ in range(Q)]


def solve(Queries, inv=False):
  if inv:
    Queries = [('-' if p == '+' else '+', d) for p, d in Queries[::-1]]

  Z = [deque() for _ in range(5001)]
  P = [None] * Q
  for i, (p, d) in enumerate(Queries):
    if p == '+':
      Z[d].append(i)
    else:
      j = Z[d].pop()
      P[i] = j
      P[j] = i

  dp = [0] * (K + 1)
  dp[0] = 1
  Ans = []

  for _ in range(Q):
    t, d = input().split()
    d = int(d)

    dp_next = dp[:]
    if t == '+':
      for i in range(d, K + 1):
        dp_next[i] += dp[i - d]
        dp_next[i] %= mod
    else:
      for i in range(d, K + 1):
        dp_next[i] -= dp[i - d]
        dp_next[i] %= mod

    dp = dp_next
    print(t, d, dp)

    Ans.append(dp[-1])

  for a in Ans:
    print(a)
