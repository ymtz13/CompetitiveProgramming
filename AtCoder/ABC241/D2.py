from bisect import bisect_left, bisect


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


Q = int(input())

queries = []
X = []
for _ in range(Q):
  q = tuple(map(int, input().split()))
  queries.append(q)

  if q[0] == 1:
    X.append(q[1])

SX = sorted(list(set(X)))
D = {x: i for i, x in enumerate(SX)}

st = SegTree(len(SX), 0, lambda x, y: x + y)

ans = []


def find(t):
  ok = len(SX)
  ng = 0
  while ok - ng > 1:
    tgt = (ok + ng) // 2
    if st.query(0, tgt + 1) >= t:
      ok = tgt
    else:
      ng = tgt

  return ok


ss = 0

for q in queries:
  t = q[0]
  if t == 1:
    x = q[1]
    i = D[x]
    st.update(D[x], st.bottom[i] + 1)
    ss += 1

  if t == 2:
    x, k = q[1:]
    j = bisect(SX, x)
    if j == 0:
      print(-1)
      continue
    i = D[SX[j - 1]]
    s = st.query(0, i + 1)
    t = s - k + 1
    if t <= 0:
      print(-1)
    else:
      v = find(t)
      print(SX[v])

  if t == 3:
    x, k = q[1:]
    j = bisect_left(SX, x)
    i = D[SX[j]]
    s = st.query(0, i)
    t = s + k
    if t > ss:
      print(-1)
    else:
      v = find(t)
      print(SX[v])