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


def f(l, r):
  lcnt = l[:26]
  rcnt = r[:26]

  lmin, lmax, lsorted = l[26:]
  rmin, rmax, rsorted = r[26:]

  tcnt = (c + d for c, d in zip(lcnt, rcnt))
  tmin = min(lmin, rmin)
  tmax = max(lmax, rmax)
  tsorted = lsorted and rsorted and lmax <= rmin

  return (*tcnt, tmin, tmax, tsorted)


tuples = [
    tuple([1 if d == c else 0 for d in range(26)] + [c, c, True])
    for c in range(26)
]

initvec = []
for i, c in enumerate(S):
  initvec.append(tuples[c])
  cnt[c] += 1

st = SegTree(N, f, (0, ) * 26 + (+INF, -INF, True), initvec)

ans = []

for _ in range(Q):
  query = input().split()
  t = int(query[0])

  if t == 1:
    x = int(query[1]) - 1
    c = ord(query[2]) - oa

    d = S[x]
    S[x] = c

    st.update(x, tuples[c])

    cnt[d] -= 1
    cnt[c] += 1

  if t == 2:
    l = int(query[1])
    r = int(query[2])

    res = st.query(l-1, r)
    tcnt = res[:26]
    tmin, tmax, tsorted = res[26:]

    if not tsorted:
      a = 'No'
    else:
      a = 'Yes'
      for c in range(tmin + 1, tmax):
        if tcnt[c] < cnt[c]: a = 'No'

    ans.append(a)

for a in ans:
  print(a)
