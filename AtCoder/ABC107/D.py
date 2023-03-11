from collections import defaultdict


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


N = int(input())
A = list(map(int, input().split()))


def f(x):
  s = 0
  offset = N + 10
  st = SegTree(offset * 2, lambda x, y: x + y, 0)
  st.update(offset, 1)
  cnt = 0

  for a in A:
    s += 1 if a >= x else -1
    cnt += st.query(0, s + offset + 1)
    st.update(s + offset, st.bottom[s + offset] + 1)

  return cnt


M = N * (N + 1) // 2
half = M // 2 if M % 2 == 0 else M // 2 + 1

ng = max(A) + 1
ok = 0
while ng - ok > 1:
  tgt = (ng + ok) // 2
  if f(tgt) >= half:
    ok = tgt
  else:
    ng = tgt

print(ok)
