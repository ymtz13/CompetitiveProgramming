H, W = map(int, input().split())
A = []

for _ in range(H):
  R = list(map(int, input().split()))
  Rwo0 = [r for r in R if r > 0]
  Rmin = min(Rwo0) if Rwo0 else 0
  Rmax = max(R)
  A.append((R, Rmin, Rmax))

  RI = [(r, i) for i, r in enumerate(R) if r > 0]
  RI.sort()

  G = []
  g = []
  p = None
  for r, i in RI:
    if g and r != p:
      G.append(g)
      g = []

    g.append(i)
    p = r

  if g: G.append(g)

  K = []
  
  print(G)

A.sort(key=lambda R: R[1:])

for row in A:
  print(row)
