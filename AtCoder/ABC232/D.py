from collections import deque

H, W = map(int, input().split())
C = [[False] * (W + 1) for _ in range(H + 1)]
D = [[None] * (W + 1) for _ in range(H + 1)]

for h in range(H):
  S = input()
  for w, c in enumerate(S):
    C[h][w] = c == '.'

queue = deque([(1, 0, 0)])
ans = 0
while queue:
  d, h, w = queue.popleft()
  if D[h][w] is not None or not C[h][w]: continue
  D[h][w] = d
  ans = max(ans, d)

  queue.append((d + 1, h + 1, w))
  queue.append((d + 1, h, w + 1))

print(ans)
