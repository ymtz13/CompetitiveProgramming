def ans(h, w):
  print(h + 1, w + 1)
  exit()


H, W = map(int, input().split())
G = [input() for _ in range(H)]
S = set()

h = w = 0
while True:
  key = h * W + w
  if key in S:
    print(-1)
    exit()
  S.add(key)

  g = G[h][w]

  if g == 'U':
    if h == 0: ans(h, w)
    h -= 1

  if g == 'D':
    if h == H - 1: ans(h, w)
    h += 1

  if g == 'L':
    if w == 0: ans(h, w)
    w -= 1

  if g == 'R':
    if w == W - 1: ans(h, w)
    w += 1
