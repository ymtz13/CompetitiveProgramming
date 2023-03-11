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


s = SegTree(100, lambda x, y: x + y, 0)

mod = 998244353

N = int(input())
A = list(map(int, input().split()))

M = 200010

stN = SegTree(M, lambda x, y: x + y, 0)
stS = SegTree(M, lambda x, y: x + y, 0)

a1 = A[0]
Ans = [a1]
stN.update(a1, 1)
stS.update(a1, a1)

for K, a in enumerate(A[1:], 2):
  K1sq = (K - 1) * (K - 1) % mod
  Ksqinv = pow(K * K, mod - 2, mod)

  ans = Ans[-1] * K1sq
  ans %= mod

  ans += a
  ans += 2 * (a * stN.query(0, a + 1) + stS.query(a + 1, M))
  ans %= mod

  ans *= Ksqinv
  ans %= mod

  stN.update(a, stN.bottom[a] + 1)
  stS.update(a, stS.bottom[a] + a)

  Ans.append(ans)

for ans in Ans:
  print(ans)
