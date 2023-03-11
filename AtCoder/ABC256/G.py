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


N, Q = map(int, input().split())
A = list(map(int, input().split()))

mod = 998244353

A0 = A
A1 = [(N - i) * a % mod for i, a in enumerate(A)]
A2 = [(N - i) * (N - i + 1) // 2 * a % mod for i, a in enumerate(A)]

st0 = SegTree(N, lambda x, y: (x + y) % mod, 0, A0)
st1 = SegTree(N, lambda x, y: (x + y) % mod, 0, A1)
st2 = SegTree(N, lambda x, y: (x + y) % mod, 0, A2)

ans = []

for _ in range(Q):
  query = tuple(map(int, input().split()))

  if query[0] == 1:
    _, i, v = query
    i -= 1
    st0.update(i, v)
    st1.update(i, (N - i) * v % mod)
    st2.update(i, (N - i) * (N - i + 1) // 2 * v % mod)

  if query[0] == 2:
    _, x = query

    c1 = x - N
    c0 = x * (x + 1) // 2 - c1 * N - N * (N + 1) // 2

    v0 = st0.query(0, x)
    v1 = st1.query(0, x)
    v2 = st2.query(0, x)

    a = v2 + c1 * v1 + c0 * v0
    ans.append(a % mod)

for a in ans:
  print(a)
