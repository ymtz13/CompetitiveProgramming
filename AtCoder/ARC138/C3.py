from heapq import heappop, heappush


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
S = sum(A)

A2 = A + A

st = SegTree(N * 2 + 10, 0, lambda x, y: x + y)
heap = []
sheap = []
s = 0
selected = [False] * N

for i in range(0, N, 2):
  heappush(heap, (A[i], i))
  heappush(heap, (A[i + 1], i + 1))

  a, j = heappop(heap)
  st.update(j, 1)
  s += a
  selected[j] = True
  heappush(sheap, (-a, j))

m = s
kk = 0
for i in range(N - 1, -1, -1):
  if selected[i]: continue

  am, j = sheap[0]
  am = -am

  #am, j = heappop(sheap)
  #am = -am

  if am >= A[i]:
    heappop(sheap)
    selected[j] = False
    selected[i] = True
    heappush(sheap, (-A[i], i))
    s += A[i] - am

  else:
    k = (i + 1) % N

    if not selected[k]:
      heappop(sheap)
      selected[j] = False
      s -= am

      if A[k] < A[i]:
        heappush(sheap, (-A[k], k))
        selected[k] = True
        s += A[k]
      else:
        heappush(sheap, (-A[i], i))
        selected[i] = True
        s += A[i]

  #m = min(m, s)
  if s < m:
    m = s
    kk = i

print(kk, S - m)
