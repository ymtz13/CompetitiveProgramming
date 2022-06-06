from heapq import heappush, heappop


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


N, X = map(int, input().split())

A = list(map(int, input().split()))

st = SegTree(N, 0, max)
for i, a in enumerate(A):
  st.update(i, a)

heap = []
for i, a in enumerate(A):
  heappush(heap, (a, i, 1))

ans = 1 << 60

for _ in range(N * 40):
  ar, i, r = heappop(heap)
  a = A[i]
  r *= 2
  heappush(heap, (((a + X) * r) - X, i, r))

  al = st.query(0, N)
  D = al - ar
  ans = min(ans, 0 if D + 1 <= X else D)

  st.update(i, a * r)

print(ans)
