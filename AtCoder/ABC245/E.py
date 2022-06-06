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


from collections import deque

N, M = map(int, input().split())
I1 = list(map(int, input().split()))
I2 = list(map(int, input().split()))
I3 = list(map(int, input().split()))
I4 = list(map(int, input().split()))

Ys = sorted(list(set(I2 + I4)))
Dist = {y: i for i, y in enumerate(Ys)}

C = list(zip(I1, I2))
B = list(zip(I3, I4))

C.sort(reverse=True)
B.sort(reverse=True)
B = deque(B)

NYs = len(Ys)
INF = 1 << 60
st = SegTree(NYs, INF, min)
count = [0] * NYs

for cx, cy in C:
  #print('cx, cy = ', cx, cy)
  while B and B[0][0] >= cx:
    bx, by = B.popleft()
    #print(bx, by)

    dby = Dist[by]
    st.update(dby, dby)
    count[dby] += 1

  dcy = Dist[cy]
  m = st.query(dcy, NYs)
  if m == INF:
    print('No')
    exit()
  count[m] -= 1
  if count[m] == 0:
    st.update(m, INF)

print('Yes')
