from collections import deque

H, W = map(int, input().split())
H2 = H + 2
W2 = W + 2
M = H2 * W2
S = ['_' * W2] + ['_{}_'.format(input()) for _ in range(H)] + ['_' * W2]

queue = deque([W2 + 1])
dist = [-1] * M

while queue:
  q = queue.popleft()
  d = q // M
  r = q % M
  h = r // W2
  w = r % W2

  if dist[r] > -1: continue
  dist[r] = d

  c = '.' if S[h][w] == '#' else '#'

  if S[h + 1][w] == c:
    queue.append(M + q + W2)
  if S[h - 1][w] == c:
    queue.append(M + q - W2)
  if S[h][w + 1] == c:
    queue.append(M + q + 1)
  if S[h][w - 1] == c:
    queue.append(M + q - 1)

print(dist[H * W2 + W])
