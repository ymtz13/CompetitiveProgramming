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


N, K = map(int, input().split())
P = list(map(int, input().split()))

C = [1]
prev = P[0]
for p in P[1:]:
  C.append(C[-1] + 1 if p > prev else 1)
  prev = p

stMax = SegTree(N, 0, max)
stMin = SegTree(N, 0, min)

for i, p in enumerate(P):
  stMax.update(i, p)
  stMin.update(i, p)

ans = 1
x = C[K - 1] >= K
for i in range(K, N):
  j = i - K
  pmax = stMax.query(j, i + 1)
  pmin = stMin.query(j, i + 1)

  if pmax != P[i] or pmin != P[j]:
    if C[i] >= K:
      if not x:
        ans += 1
        x = True

    else:
      ans += 1

print(ans)
