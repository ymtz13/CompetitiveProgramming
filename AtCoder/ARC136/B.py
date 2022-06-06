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


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

SA = sorted(A)
SB = sorted(B)
if SA != SB:
  print('No')
  exit()

if len(set(A)) < N:
  print('Yes')
  exit()

D = {v: i for i, v in enumerate(SA)}

DA = [D[a] for a in A]
DB = [D[b] for b in B]

stA = SegTree(N, 0, lambda x, y: x + y)
cA = 0
for v in DA:
  cA += stA.query(v, N)
  stA.update(v, 1)

stB = SegTree(N, 0, lambda x, y: x + y)
cB = 0
for v in DB:
  cB += stB.query(v, N)
  stB.update(v, 1)

print('Yes' if (cA + cB) % 2 == 0 else 'No')
