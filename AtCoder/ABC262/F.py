from heapq import heappop, heappush


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


def remove(A, n):
  if len(A) <= n: return []
  t = len(A) - n

  heap = []
  heappush(heap, (A[0], 0))
  i = 1
  l = -1

  retval = []
  while n > 0:
    for _ in range(n - (i - l - 2)):
      heappush(heap, (A[i], i))
      i += 1

    while True:
      m, j = heappop(heap)
      if j > l: break

    retval.append(m)
    n -= j - l - 1
    l = j

    if len(retval) == t: return retval

  return retval + A[l + 1:]


N, K = map(int, input().split())
P = list(map(int, input().split()))

if K == 0:
  print(' '.join(map(str, P)))
  exit()

m0 = min(P[:K + 1])
m1 = min(P[-K:])


def solve0(N, K, P, m):
  for i in range(N):
    if P[i] == m: break

  return [m] + remove(P[i + 1:], K - i)


def solve1(N, K, P, m):
  for i in range(N):
    if P[i] == m: break

  PF = P[i + 1:]
  PB = P[:i]

  XB = remove(PB, K - len(PF) - 1)
  XB0 = XB[0] if XB else 1 << 60

  s = SegTree(len(PF), min, 1 << 60, PF)
  ss = set()

  XF = []
  for i, _ in enumerate(PF):
    q = s.query(i, len(PF))
    if q not in ss and q < XB0:
      ss.add(q)
      XF.append(q)

  return [m] + XF + XB


s0 = solve0(N, K, P, m0)
s1 = solve1(N, K, P, m1)
print(' '.join(map(str, min(s0, s1))))
