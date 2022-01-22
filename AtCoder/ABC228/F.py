class SegTree:
  def __init__(self, N, fill, function):
    L = 1
    M = 1
    while M < N:
      L += 1
      M <<= 1

    segsize = [None] * L
    data = [None] * L
    for l in range(L):
      segsize[l] = 1 << l
      data[l] = [fill] * (M // segsize[l])

    self.L = L
    self.segsize = segsize
    self.data = data
    self.function = function
    self.bottom = self.data[0]

    self.zip = [(l, segsize[l], data[l]) for l in range(L)]

  def update(self, i, value):
    function = self.function
    layer = self.bottom
    layer[i] = value

    for layer_above in self.data[1:]:
      i >>= 1
      j = i << 1
      layer_above[i] = function(layer[j], layer[j + 1])
      layer = layer_above

  def query(self, qbgn, qend):
    vals = []
    #segs = []

    q = qbgn
    for l, ssize, data in self.zip:
      if q & ssize and q + ssize <= qend:
        #segs.append((q, ssize))
        vals.append(data[q >> l])
        q += ssize

    for l, ssize, data in reversed(self.zip):
      if q + ssize <= qend:
        #segs.append((q, ssize))
        vals.append(data[q >> l])
        q += ssize

    retval = vals[0]
    for val in vals[1:]:
      retval = self.function(retval, val)

    #return segs
    return retval

  def __str__(self):
    s = []
    for l, row in enumerate(self.data[::-1]):
      s.append('{:2d} {}'.format(l, row))
    return '\n'.join(s)


s = SegTree(100, 0, lambda x, y: x + y)

s.update(5, 6)
s.update(9, 7)
s.update(3, 3)

H, W, h1, w1, h2, w2 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

h2 = min(h1, h2)
w2 = min(w1, w2)

T = [[0] * (W + 1) for _ in range(H)]
for Arow, Trow in zip(A, T):
  for w in range(1, W + 1):
    Trow[w] = Trow[w - 1] + Arow[w - 1]

S = [[0] * (W + 1) for _ in range(H + 1)]
for h in range(H):
  for w in range(1, W + 1):
    S[h + 1][w] = S[h][w] + T[h][w]

S1 = [[None] * (W - w1 + 1) for _ in range(H - h1 + 1)]
#S2 = [[None] * (W - w2 + 1) for _ in range(H - h2 + 1)]
S2 = [SegTree(1024, 0, max) for _ in range(H - h2 + 1)]
for h in range(H - h2 + 1):
  for w in range(W - w2 + 1):
    #S2[h][w] = S[h + h2][w + w2] - S[h][w]
    S2[h].update(w, S[h + h2][w + w2] + S[h][w] - S[h + h2][w] - S[h][w + w2])

st = SegTree(1024, 0, max)
#st = SegTree(16, 0, max)

ans = 0

for w in range(W - w1 + 1):
  for h in range(H - h2 + 1):
    st.update(h, S2[h].query(w, w + w1 - w2 + 1))


  for h in range(H - h1 + 1):
    ss = S[h + h1][w + w1] + S[h][w] - S[h + h1][w] - S[h][w + w1]

    mm = st.query(h, h + h1 - h2 + 1)

    ans = max(ans, ss - mm)

print(ans)
