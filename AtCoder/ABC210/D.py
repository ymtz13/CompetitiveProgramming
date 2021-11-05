INF = 10**10

H, W, C =  map(int, input().split())
A = [[INF]*(W+2)] + [[INF] + list(map(int, input().split())) + [INF] for _ in range(H)] + [[INF]*(W+2)]
Arev = [a[::-1] for a in A]

def solve(A):
  dp = [[INF]*(W+2) for _ in range(H+2)]
  ans = INF
  for h in range(1, H+1):
    for w in range(1, W+1):
      cost = min(dp[h-1][w]+C, dp[h][w-1]+C)
      ans = min(ans, cost + A[h][w])
      dp[h][w] = min(A[h][w], cost)

  return ans

ansR = solve(A)
ansL = solve(Arev)

print(min(ansR, ansL))
