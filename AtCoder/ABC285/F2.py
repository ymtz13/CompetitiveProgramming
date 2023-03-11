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

N = int(input())
S = [ord(c) - oa for c in input()]
Q = int(input())

cnt = [0] * 26

sts = [SegTree(N, lambda x, y: x + y, 0) for _ in range(26)]
for i, c in enumerate(S):
  sts[c].update(i, 1)
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

    sts[d].update(x, 0)
    sts[c].update(x, 1)

    cnt[d] -= 1
    cnt[c] += 1

  if t == 2:
    l = int(query[1])
    r = int(query[2])

    scnt = []
    cmin = cmax = None
    for c, st in enumerate(sts):
      n = st.query(l - 1, r)
      scnt.append(n)

      if n and cmin is None: cmin = c
      if n: cmax = c

    print(cnt, scnt, cmin, cmax)

    a = 'Yes'
    for c in range(cmin + 1, cmax):
      if scnt[c] < cnt[c]: ans = 'No'

    ans.append(a)

for a in ans:
  print(a)
