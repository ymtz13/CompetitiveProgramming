from collections import deque

H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
C = [[None] * (W + 2) for _ in range(H + 2)]

for w in range(W + 2):
  C[0][w] = C[-1][w] = -1
for h in range(H + 2):
  C[h][0] = C[h][-1] = -1
for h in range(1, H + 1):
  S = input()
  for w, c in enumerate(S, 1):
    if c == '@': C[h][w] = -1

queue = deque([
    (x1 + 1, y1, 1, +1, 0),
    (x1 - 1, y1, 1, -1, 0),
    (x1, y1 + 1, 1, 0, +1),
    (x1, y1 - 1, 1, 0, -1),
])


def printC():
  for row in C:
    R = ['.' if c is None else '@' if c == -1 else str(c) for c in row]
    print(''.join(R))


C[x1][y1] = 0

while queue:
  x0, y0, d, dx, dy = queue.popleft()
  dxL, dyL = -dy, dx
  dxR, dyR = dy, -dx

  for k in range(K):
    x = x0 + dx * k
    y = y0 + dy * k
    if C[x][y] is not None:
      if C[x][y] < d:
        k = -1
        break
      continue

    C[x][y] = d

    queue.append((x + dxL, y + dyL, d + 1, dxL, dyL))
    queue.append((x + dxR, y + dyR, d + 1, dxR, dyR))

  if k == K - 1:
    queue.append((x + dx, y + dy, d + 1, dx, dy))

ans = C[x2][y2]
print(ans if ans is not None else -1)
