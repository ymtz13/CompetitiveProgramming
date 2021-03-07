N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 10**20

for K in range(N, 0, -1):
  dp = [[None]*K for _ in range(K+1)]
  dp[0][0] = 0
  for a in A:
    for k in range(K, 0, -1):
      dp2 = dp[k][:]
      for r, v in enumerate(dp[k-1]):
        if v is not None:
          r2 = (v+a)%K
          dp2[r2] = max(dp2[r2], v + a) if dp2[r2] is not None else v + a
      dp[k] = dp2

  #print('K: ', K)
  #for k in range(K+1):
  #  print(k, dp[k])
  
  R = X % K
  if dp[K][R] is not None:
    ans = min(ans, (X - dp[K][R]) // K)
    #break

print(ans)
