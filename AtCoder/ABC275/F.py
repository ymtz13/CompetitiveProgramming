N, M = map(int, input().split())
A = list(map(int, input().split()))

INF = 9999

dp0 = [INF] * (M + 1)
dp1 = [INF] * (M + 1)
dp0[0] = 0

for a in A:
  dp0_next = [INF] * (M + 1)
  dp1_next = [INF] * (M + 1)
  dp0_next[0] = 1

  for m in range(1, M + 1):
    dp0_next[m] = min(dp0[m], dp1[m] + 1)

  for m in range(a, M + 1):
    dp1_next[m] = min(dp0[m - a], dp1[m - a])

  dp0 = dp0_next
  dp1 = dp1_next

  #print(dp0)
  #print(dp1)
  #print()

for v0, v1 in zip(dp0[1:], dp1[1:]):
  ans = min(v0, v1)
  print(-1 if ans >= INF else ans)
