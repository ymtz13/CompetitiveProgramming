H, W = map(int, input().split())

px = py = None
for h in range(H):
  S = input()
  for w, c in enumerate(S):
    if c == 'o':
      if px is None:
        px = w
        py = h

      else:
        print(abs(px - w) + abs(py - h))
        exit()
