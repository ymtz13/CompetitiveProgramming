from collections import defaultdict, deque

class SegTree:
  def __init__(self, N, fill, function):
    L = 1
    k = 1
    while k<N:
      L += 1
      k<<=1

    segsize = [None]*L
    data = [None]*L
    for l in range(L):
      segsize[l] = 1<<(L-l-1)
      data[l] = [fill]*(1<<l)

    self.L = L
    self.segsize = segsize
    self.data = data
    self.function = function
    self.bottom = self.data[-1]

  def update(self, i, value):
    self.bottom[i] = value
        
    for l in range(self.L-2, -1, -1):
      i//=2
      self.data[l][i] = self.function(*self.data[l+1][i*2:i*2+2])
            
  def query(self, ibgn, iend, l=0):
    if iend<=ibgn: return 0

    ssize = self.segsize[l]
    if ibgn%ssize==0 and iend-ibgn==ssize: return self.data[l][ibgn//ssize]

    imid = ibgn - ibgn%ssize + ssize//2
    if iend<=imid or imid<=ibgn:
      return self.query(ibgn, iend, l+1)
    return self.function(
      self.query(ibgn, imid, l+1),
      self.query(imid, iend, l+1)
    )

N = int(input())
A = [i + int(a) for i, a in enumerate(input().split())]
B = [i + int(b) for i, b in enumerate(input().split())]

D = defaultdict(deque)
for i, a in enumerate(A):
  D[a].append(i)

#print(A, B, D)

L = [None]*N

for i, b in enumerate(B):
  q = D[b]
  if q:
    l = q.popleft()
    L[l] = i
  else:
    print(-1)
    exit()

#print(L)

s = SegTree(N+5, 0, lambda a, b: a+b)
ans = 0
for l in L[::-1]:
  ans += s.query(0, l)
  s.update(l, 1)

print(ans)
