INF = 1 << 60

N, K = map(int, input().split())
A = list(map(int, input().split()))
P = [tuple(map(int, input().split())) for _ in range(N)]

dsqmax = 0
for x, y in P:
  dsqmin = INF
  for a in A:
    ax, ay = P[a - 1]
    dx = x - ax
    dy = y - ay
    dsq = dx * dx + dy * dy
    dsqmin = min(dsqmin, dsq)

  dsqmax = max(dsqmax, dsqmin)

print(dsqmax**0.5)
