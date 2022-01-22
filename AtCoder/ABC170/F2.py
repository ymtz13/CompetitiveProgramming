from heapq import heappush, heappop

H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
Cx = [[None] * (W + 2) for _ in range(H + 2)]
Cy = [[None] * (W + 2) for _ in range(H + 2)]

T = 1 << 20

for w in range(W + 2):
  Cx[0][w] = Cx[-1][w] = Cy[0][w] = Cy[-1][w] = -1
for h in range(H + 2):
  Cx[h][0] = Cx[h][-1] = Cy[h][0] = Cy[h][-1] = -1
for h in range(1, H + 1):
  S = input()
  for w, c in enumerate(S, 1):
    if c == '@': Cx[h][w] = Cy[h][w] = -1

C = [Cx, Cy]
queue = [(1, 0, 0, x1, y1), (1, 0, 1, x1, y1)]

for cx in Cx:
  print(['.' if c is None else '@' for c in cx])
print()
for cy in Cy:
  print(''.join(['.' if c is None else '@' for c in cy]))

while queue:
  s, t, l, x, y = heappop(queue)
  if C[l][x][y] is not None: continue
  C[l][x][y] = (s, t)

  print(l, x, y, '(s, t) = ', s, t)

  ss = s + 1 if t == K else s
  tt = t + 1 if t < K else 1

  if l == 0:
    if Cx[x + 1][y] is None: heappush(queue, (ss, tt, 0, x + 1, y))
    if Cx[x - 1][y] is None: heappush(queue, (ss, tt, 0, x - 1, y))
    if Cy[x][y] is None: heappush(queue, (s + 1, 0, 1, x, y))

  if l == 1:
    if Cy[x][y + 1] is None: heappush(queue, (ss, tt, 1, x, y + 1))
    if Cy[x][y - 1] is None: heappush(queue, (ss, tt, 1, x, y - 1))
    if Cx[x][y] is None: heappush(queue, (s + 1, 0, 0, x, y))

INF = 1 << 60
sx, _ = Cx[x2][y2] or (INF, 0)
sy, _ = Cy[x2][y2] or (INF, 0)

ans = min(sx, sy)
print(ans if ans < INF else -1)

#print(Cx[x2][y2], Cy[x2][y2])
