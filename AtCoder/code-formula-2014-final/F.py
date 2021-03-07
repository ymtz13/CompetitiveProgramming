x = y = 0
for r in range(1, 101):
  if 1500-y < 2*r:
    x += (r-1)*2
    y = 0
  print(x+r, y+r)
  y += 2*r