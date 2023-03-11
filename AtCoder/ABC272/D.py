from collections import deque


def f(M):
  P = []
  dx = M
  for dy in range(0, M + 1):
    dysq = dy * dy
    if dysq > M: break

    while dx > 0 and dx * dx + dysq > M:
      dx -= 1

    if dx * dx + dy * dy == M:
      P.append((dy, dx))

  return P


N, M = map(int, input().split())
P = f(M)

Nsq = N * N
ans = [-1] * Nsq
queue = deque([0])

while queue:
  q = queue.popleft()
  d = q // Nsq
  r = q % Nsq
  x = r // N
  y = r % N

  if ans[r] != -1: continue
  ans[r] = d

  D = []
  for dx, dy in P:
    D.append((x + dx, y + dy, d + 1))
    D.append((x + dx, y - dy, d + 1))
    D.append((x - dx, y + dy, d + 1))
    D.append((x - dx, y - dy, d + 1))

  for x, y, d in D:
    if x < 0 or x >= N: continue
    if y < 0 or y >= N: continue

    r = x * N + y
    if ans[r] != -1: continue

    queue.append(d * Nsq + r)

for row in range(N):
  print(' '.join(map(str, ans[row * N:(row + 1) * N])))
