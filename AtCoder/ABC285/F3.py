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


oa = ord('a')

INF = 1 << 30

N = int(input())
S = [ord(c) - oa for c in input()]
Q = int(input())

cnt = [0] * 26

sts_min = [SegTree(N, min, +INF) for _ in range(26)]
sts_max = [SegTree(N, max, -INF) for _ in range(26)]
for i, c in enumerate(S):
  sts_min[c].update(i, i)
  sts_max[c].update(i, i)
  cnt[c] += 1

ans = []

for _ in range(Q):
  query = input().split()
  t = int(query[0])

  if t == 1:
    x = int(query[1]) - 1
    c = ord(query[2]) - oa

    d = S[x]
    S[x] = c

    sts_min[d].update(x, +INF)
    sts_max[d].update(x, -INF)
    sts_min[c].update(x, x)
    sts_max[c].update(x, x)

    cnt[d] -= 1
    cnt[c] += 1

  if t == 2:
    l = int(query[1])
    r = int(query[2])

    sorted = True
    scnt = []
    cmin = cmax = None
    prevmax = -1
    for c, (stmin, stmax) in enumerate(zip(sts_min, sts_max)):
      xmin = stmin.query(l - 1, r)
      xmax = stmax.query(l - 1, r)

      n = xmax - xmin + 1 if xmin < INF else 0
      scnt.append(n)

      if not n: continue

      if xmin < prevmax:
        sorted = False
        break
      prevmax = xmax

      if cmin is None: cmin = c
      cmax = c

    if not sorted:
      a = 'No'
    else:
      a = 'Yes'
      for c in range(cmin + 1, cmax):
        if scnt[c] < cnt[c]: a = 'No'

    ans.append(a)

for a in ans:
  print(a)
