class SegTree:
  def __init__(self, N, function, identity, initialData=None):
    L = 1
    M = 1
    while M < N:
      L += 1
      M <<= 1

    segsize = [1 << l for l in range(L)]
    data = [None] * L

    if initialData:
      layer = data[0] = initialData[:M] + [identity] * (M - len(initialData))
      for i in range(1, L):
        layer = data[i] = [function(*v) for v in zip(layer[0::2], layer[1::2])]

    else:
      for l in range(L):
        data[l] = [identity] * (M // segsize[l])

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


INF = 1 << 60

Q, A, B = map(int, input().split())

query = [(1, A, B)] + [tuple(map(int, input().split())) for _ in range(Q)]

V = set()
for t, a, b in query:
  if t == 1:
    V.add(a - b)
    V.add(a + b)
  else:
    V.add(a)
    V.add(b)

V = list(V)
V.sort()

M = len(V)
D = {v: i for i, v in enumerate(V)}

stmax = SegTree(M, max, -INF)
stmin = SegTree(M, min, +INF)

Ans = []

for t, a, b in query:
  if t == 1:
    v1 = a - b
    v2 = a + b
    i1 = D[v1]
    i2 = D[v2]
    stmax.update(i1, v1)
    stmin.update(i1, v1)
    stmax.update(i2, v2)
    stmin.update(i2, v2)

  if t == 2:
    il = D[a]
    ir = D[b]

    if stmax.query(il, ir + 1) != -INF:
      Ans.append(0)
      continue

    vl = stmax.query(0, il + 1)
    vr = stmin.query(ir, M)

    Ans.append(min(a - vl, vr - b))

for ans in Ans:
  print(ans)
