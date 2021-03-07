H, W = map(int, input().split())
Sb = [[0] for _ in range(H)]
Sw = [[0] for _ in range(H)]
for h in range(H):
  C = map(int, input().split())
  sb = sw = 0
  for w, c in enumerate(C):
    if (h+w)%2==0:
      sb += c
    else:
      sw += c
    Sb[h].append(sb)
    Sw[h].append(sw)

ans = 0
for R in range(1, W+1):
  for L in range(R):
    d = 0
    D = [None] * 30000
    D[0] = -1
    for h, (sb, sw) in enumerate(zip(Sb, Sw)):
      nb = sb[R] - sb[L]
      nw = sw[R] - sw[L]
      d += nb - nw
      if D[d] is not None:
        ans = max(ans, (R-L)*(h-D[d]))
      else:
        D[d] = h

    

print(ans)