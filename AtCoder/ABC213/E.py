from collections import deque

H, W = map(int, input().split())
H6 = H + 6
W6 = W + 6
M = [[2] * W6 for _ in range(H6)]
for h in range(3, H + 3):
  S = input()
  for w, c in enumerate(S, 3):
    M[h][w] = 0 if c == '.' else 1

nb = (
    (+1, +0),
    (-1, +0),
    (+0, +1),
    (+0, -1),
    (+1, +1),
    (+1, -1),
    (-1, +1),
    (-1, -1),
    (+2, +1),
    (+2, +0),
    (+2, -1),
    (-2, +1),
    (-2, +0),
    (-2, -1),
    (+1, +2),
    (+0, +2),
    (-1, +2),
    (+1, -2),
    (+0, -2),
    (-1, -2),
)

D = [[None] * W6 for _ in range(H6)]
queue = deque([(3, 3)])
reached = []

for d in range(H6 * W6):
  while queue:
    h, w = queue.popleft()
    if M[h][w] != 0 or D[h][w] is not None: continue
    D[h][w] = d
    reached.append((h, w))

    queue.append((h + 1, w))
    queue.append((h - 1, w))
    queue.append((h, w + 1))
    queue.append((h, w - 1))

  queue = deque()
  reached_next = []
  for h, w in reached:
    for dh, dw in nb:
      hh = h + dh
      ww = w + dw
      if M[hh][ww] == 2 or D[hh][ww] is not None: continue
      D[hh][ww] = d + 1
      reached_next.append((hh, ww))
      queue.append((hh + 1, ww))
      queue.append((hh - 1, ww))
      queue.append((hh, ww + 1))
      queue.append((hh, ww - 1))
  
  reached = reached_next

#for d in D:
#  dd = ["{}".format(dd if dd is not None else ' ') for dd in d]
#  print(''.join(dd))

print(D[H + 2][W + 2])
