N = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))


def f(n, S, B):
  dp = list(range(n + 1))
  for s, b in zip(S, B):
    for i in range(s, n + 1):
      dp[i] = max(dp[i], dp[i - s] + b)
  return dp[n]


mid = f(N, A, B)
print(mid)
ans = f(mid, B, A)
print(ans)
