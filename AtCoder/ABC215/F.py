N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
K = 1 << 32


def solve(P):
  P = sorted(P, key=lambda p: -(p[0] + p[1]) * K + p[1])

  m = 0
  ymin = 1 << 60
  for _, y in P:
    if ymin < y:
      m = max(m, y - ymin)
    else:
      ymin = y

  return m


ans = 0
for _ in range(2):
  for _ in range(2):
    ans = max(ans, solve(P))
    P = [(-y, x) for x, y in P]
  P = [(-x, y) for x, y in P]

print(ans)
