from collections import deque

H, W, K = map(int, input().split())
A = [input() for _ in range(H)]
for h in range(H):
  for w in range(W):
    if A[h][w] == 'S':
      sh = h
      sw = w

visited = [[False] * W for _ in range(H)]

queue = deque([(sh, sw, 0)])
ans = 1 << 60
while queue:
  h, w, d = queue.popleft()
  if visited[h][w] or A[h][w] == '#': continue
  visited[h][w] = True

  ans = min(ans, (min(h, w, H - 1 - h, W - 1 - w) + K - 1) // K + 1)
  if ans == 1: break

  if d < K:
    queue.append((h - 1, w, d + 1))
    queue.append((h + 1, w, d + 1))
    queue.append((h, w - 1, d + 1))
    queue.append((h, w + 1, d + 1))

print(ans)
