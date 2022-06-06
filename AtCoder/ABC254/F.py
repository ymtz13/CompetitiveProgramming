from math import gcd


class SegTree:
  def __init__(self, N, fill, function):
    L = 1
    M = 1
    while M < N:
      L += 1
      M <<= 1

    segsize = [None] * L
    data = [[]]
    for l in range(L):
      segsize[l] = 1 << l

    self.L = L
    self.M = M
    self.fill = fill
    self.segsize = segsize
    self.data = data
    self.function = function
    self.bottom = self.data[0]

  def init(self, bottom):
    function = self.function
    layer = self.data[0] = bottom + [0] * (self.M - len(bottom))
    print(layer)

    for i in range(self.L - 1):
      layer = self.data[i + 1] = [
          function(*v) for v in zip(layer[0::2], layer[1::2])
      ]

    self.zip = [(l, self.segsize[l], self.data[l]) for l in range(self.L)]

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
B = list(map(int, input().split()))

DA = [abs(a1 - a0) for a1, a0 in zip(A[1:], A[:-1])]
DB = [abs(b1 - b0) for b1, b0 in zip(B[1:], B[:-1])]

stMinA = SegTree(N, 0, min)
stMinB = SegTree(N, 0, min)

stMinA.init(A)
stMinB.init(B)

stDA = SegTree(N, 0, gcd)
stDB = SegTree(N, 0, gcd)

stDA.init(DA)
stDB.init(DB)

ans = []
for _ in range(Q):
  h1, h2, w1, w2 = map(int, input().split())

  mA = stMinA.query(h1 - 1, h2)
  mB = stMinB.query(w1 - 1, w2)
  m = mA + mB

  gA = stDA.query(h1 - 1, h2 - 1) if h1 != h2 else 0
  gB = stDB.query(w1 - 1, w2 - 1) if w1 != w2 else 0
  ans.append(gcd(gcd(gA, gB), m))

for a in ans:
  print(a)
