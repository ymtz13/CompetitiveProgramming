N, P = map(int, input().split())
AB = sorted([tuple(map(int, input().split())) for _ in range(N)], reverse=True)

dp = [-1]*5101
dp[0] = 0
ans = 0
for a, b in AB:
  for i, v in enumerate(dp[:a-1:-1]):
    i = 5100 - i
    j = i - a
    if j > P: continue
    x = dp[j]
    if x==-1: continue
    dp[i] = max(v, x + b)

  ans = max(ans, max(dp))

print(ans)