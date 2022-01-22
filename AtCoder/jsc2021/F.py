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


NA, NB, Q = map(int, input().split())
TXY = [tuple(map(int, input().split())) for _ in range(Q)]

S = {Y for _, _, Y in TXY}
D = {Y: i for i, Y in enumerate(sorted(list(S) + [0]))}
M = len(D)

YA = [0] * NA
YB = [0] * NB

CA = SegTree(M, 0, lambda vl, vr: vl + vr)
CB = SegTree(M, 0, lambda vl, vr: vl + vr)
SA = SegTree(M, 0, lambda vl, vr: vl + vr)
SB = SegTree(M, 0, lambda vl, vr: vl + vr)

ans = 0

for T, X, Y in TXY:
  if T == 1:
    YP = YA
    CP = CA
    CQ = CB
    SP = SA
    SQ = SB
    NQ = NB
  else:
    YP = YB
    CP = CB
    CQ = CA
    SP = SB
    SQ = SA
    NQ = NA

  Yold = YP[X - 1]
  Ynew = Y
  iYold = D[Yold]
  iYnew = D[Ynew]
  YP[X - 1] = Ynew

  c = CQ.query(iYold, M)
  s = SQ.query(iYold, M)
  ans -= s + Yold * (NQ - c)

  CP.update(iYold, CP.bottom[iYold] - 1)
  SP.update(iYold, SP.bottom[iYold] - Yold)

  c = CQ.query(iYnew, M)
  s = SQ.query(iYnew, M)
  ans += s + Ynew * (NQ - c)

  CP.update(iYnew, CP.bottom[iYnew] + 1)
  SP.update(iYnew, SP.bottom[iYnew] + Ynew)

  print(ans)

