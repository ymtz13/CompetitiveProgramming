from collections import deque

a, N = map(int, input().split())

M = 1000000
dist = [None] * M
queue = deque([(1, 0)])

while queue:
  q, d = queue.popleft()
  if q >= M or dist[q] is not None: continue
  dist[q] = d

  queue.append((q * a, d + 1))

  s = str(q)
  if q % 10 > 0:
    queue.append((int(s[-1] + s[:-1]), d + 1))

print(dist[N] or -1)
