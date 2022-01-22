N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0

for x1, y1 in P:
  for x2, y2 in P:
    dx = x1 - x2
    dy = y1 - y2
    ans = max(ans, dx * dx + dy * dy)

print(ans**0.5)
