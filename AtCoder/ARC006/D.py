H, W = map(int, input().split())
S = [input() for _ in range(H)]

XA = ((+1, -1, 1, 1), (+1, +1, 1, 1), (+2, -2, 3, 1), (+2, +2, 3, 1), (+3, -1,
                                                                       1, 3))

XB = ((-1, -4, 1, 4), (0, -4, 4, 1), (+1, -3, 1, 3), (+2, 0, 1, 1), (+3, -3, 1,
                                                                     3))

XC = ((-1, -3, 1, 3), (0, -4, 3, 1), (+3, -3, 1, 3), (+2, 0, 1, 1))

XX = ((XA, -1, -3), (XB, -2, -5), (XC, -2, -5))


def count(S):
  H = len(S)
  W = len(S[0])

  A = []
  for row in S:
    aa = [0]
    s = 0
    for c in row:
      if c == 'o': s += 1
      aa.append(s)
    A.append(aa)

  visited = [[False] * W for _ in range(H)]
  M = [None] * (H * W)

  Q = []

  for ht, (row, visrow) in enumerate(zip(S, visited)):
    for wl, (c, vv) in enumerate(zip(row, visrow)):
      if c == '.' or vv: continue

      wr = wl + 1
      while wr < W and row[wr] == 'o' and not visrow[wr]:
        wr += 1

      width = wr - wl

      hb = ht + 1
      while hb < H and A[hb][wr] - A[hb][wl] == width:
        hb += 1

      height = hb - ht

      M[ht * W + wl] = (height, width)
      if height == width: Q.append((ht, wl, height))

      for visrowx in visited[ht:hb]:
        for ww in range(wl, wr):
          visrowx[ww] = True

  cnt = [0, 0, 0]
  for h, w, scale in Q:
    for i, (X, oh, ow) in enumerate(XX):
      ph = h + scale * oh
      pw = w + scale * ow
      qh = ph + scale * 7
      qw = pw + scale * 7

      if ph < 0 or pw < 0 or qh > H or qw > W: continue

      ok = True
      for dh, dw, xh, xw in X:
        vh = h + scale * dh
        vw = w + scale * dw

        vm = M[vh * W + vw]
        if not vm or vm[0] != xh * scale or vm[1] != xw * scale:
          ok = False
          break

      if ok:
        cnt[i] += 1
        break

  return cnt


def rot(S):
  return [''.join(s) for s in zip(*reversed(S))]


nA = nB = nC = 0
for _ in range(4):
  a, b, c = count(S)
  nA += a
  nB += b
  nC += c

  S = rot(S)

print(nA, nB, nC)
