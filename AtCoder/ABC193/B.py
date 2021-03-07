N = int(input())
ans = INF = 10**10
for _ in range(N):
  A, P, X = map(int, input().split())
  if X>A: ans = min(ans, P)

print(ans if ans!=INF else -1)
