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
print(s)

s.update(5, 6)
s.update(9, 7)
s.update(3, 3)

print(s)

arr = [0] * 100
arr[5] = 6
arr[9] = 7
arr[3] = 3


def flat(segs):
  retval = []
  for q, ssize in segs:
    retval.extend(list(range(q, q + ssize)))
  return retval


def test(segs, qbgn, qend):
  assert flat(segs) == list(range(qbgn, qend))
  cnt = [0] * 1000
  for _, ssize in segs:
    cnt[ssize] += 1
  assert max(cnt) <= 2


def testval(retval, qbgn, qend):
  assert retval == sum(arr[qbgn:qend])


for qbgn in range(10):
  for qend in range(qbgn + 1, 101):
    #test(s.query(qbgn, qend), qbgn, qend)
    #print(qbgn, qend, s.query(qbgn, qend))
    testval(s.query(qbgn, qend), qbgn, qend)
