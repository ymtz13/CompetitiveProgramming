from collections import deque

H, W = map(int, input().split())
H2 = H + 2
W2 = W + 2

C = [False] * (H2 * W2)

for h in range(1, H + 1):
  for w, c in enumerate(input(), 1):
    if c == '.':
      C[h * W2 + w] = True

    elif c == 'S':
      s = h * W2 + w

sn = [s - W2, s + W2, s - 1, s + 1]

for ist in range(4):
  for igl in range(ist + 1, 4):
    st = sn[ist]
    gl = sn[igl]

    if not C[st] or not C[gl]: continue

    queue = deque([st])
    visited = [False] * (H2 * W2)

    while queue:
      q = queue.popleft()
      if not C[q] or visited[q]: continue
      visited[q] = True

      if q == gl:
        print('Yes')
        exit()

      queue.append(q - W2)
      queue.append(q + W2)
      queue.append(q - 1)
      queue.append(q + 1)

print('No')
