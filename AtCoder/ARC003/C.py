from collections import deque

H, W = map(int, input().split())
H = H + 2
W = W + 2

P = [pow(0.99, t) for t in range(250010)]

D = {str(d): d for d in range(1, 10)}
D['s'] = -1
D['g'] = -2
C = [None] * (H * W)
for h in range(1, H - 1):
  for w, c in enumerate(input(), 1):
    if c == '#': continue
    i = h * W + w
    if c == 's': s = i
    if c == 'g': g = i
    C[i] = D[c]


def check(b):
  queue = deque([(0, s)])
  visited = [False] * (W * H)
  while queue:
    t, q = queue.popleft()
    #if visited[q]: continue
    #visited[q] = True

    c = C[q]
    if c is None: continue
    if c == -2: return True
    if c > 0 and c * P[t] < b: continue

    for p in (q - W, q + W, q - 1, q + 1):
      if visited[p]: continue
      queue.append((t + 1, p))
      visited[p] = True

    #queue.append((t + 1, q - W))
    #queue.append((t + 1, q + W))
    #queue.append((t + 1, q - 1))
    #queue.append((t + 1, q + 1))

  return False


ok = -1
ng = 10
while ng - ok > 1e-9:
  tgt = (ok + ng) / 2
  if check(tgt):
    ok = tgt
  else:
    ng = tgt

print(ok if ok > -1 else -1)
