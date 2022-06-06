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


N, M, NQ = map(int, input().split())
Q = [tuple(map(int, input().split())) for _ in range(NQ)]

Z = [[] for _ in range(NQ)]
R = [None] * (N + 1)

for k, q in enumerate(Q):
  if q[0] == 2:
    _, i, x = q
    R[i] = k

  if q[0] == 3:
    _, i, j = q
    r = R[i]
    if r is not None:
      Z[r].append((k, j))

O = [0] * NQ
st = SegTree(M + 10, 0, lambda x, y: x + y)
ans = []

for k, q in enumerate(Q):
  if q[0] == 1:
    _, l, r, x = q
    st.update(l, x + st.bottom[l])
    st.update(r + 1, -x + st.bottom[r + 1])

  if q[0] == 2:
    _, i, x = q
    z = Z[k]
    for p, j in z:
      O[p] = x - st.query(0, j + 1)

  if q[0] == 3:
    _, i, j = q
    ans.append(st.query(0, j + 1) + O[k])

for a in ans:
  print(a)
