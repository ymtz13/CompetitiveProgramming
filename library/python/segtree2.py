class SegTree:
  def __init__(self, N, fill, function):
    L = 1
    k = 1
    while k < N:
      L += 1
      k <<= 1

    segsize = [None] * L
    data = [None] * L
    for l in range(L):
      segsize[l] = 1 << l
      data[l] = [fill] * (L - 1 - l)

    self.L = L
    self.segsize = segsize
    self.data = data
    self.function = function
    self.bottom = self.data[0]

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
    for l in range(self.L):
      mid = 1 << l
      if (qbgn ^ qend) & mid: break
    
    lvals = []
    rvals = []

    for i in range(l):
      if (qend-mid): break

    pass

  def __str__(self):
    s = []
    for l, row in enumerate(self.data[::-1]):
      s.append('{:2d} {}'.format(l, row))
    return '\n'.join(s)


s = SegTree(10, 0, max)
s.update2(5, 6)
s.update2(9, 7)
s.update2(3, 3)

print(s)

print(s.query(2, 6))
print(s.query3(2, 6))

for qbgn in range(10):
  for qend in range(qbgn + 2, 10):
    v = s.query(qbgn, qend)
    v3 = s.query3(qbgn, qend)
    assert v == v3, (qbgn, qend, v, v3)

# query2 は query より速い
# update2 は update より速い
