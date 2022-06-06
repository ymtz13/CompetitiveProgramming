class UF:
  def __init__(self, N):
    self.uf = [-1] * N
    self.n = N

  def find(self, x):
    if self.uf[x] < 0: return x
    self.uf[x] = self.find(self.uf[x])
    return self.uf[x]

  def size(self, x):
    return -self.uf[self.find(x)]

  def union(self, x, y):
    x, y = self.find(x), self.find(y)
    if x == y: return
    if self.size(x) > self.size(y): x, y = y, x
    self.uf[y] += self.uf[x]
    self.uf[x] = y
    self.n -= 1


N, M = map(int, input().split())
D = list(map(int, input().split()))

uf = UF(N)

E = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A - 1].append(B - 1)
  E[B - 1].append(A - 1)

  if uf.find(A - 1) == uf.find(B - 1):
    print(-1)
    exit()

  uf.union(A - 1, B - 1)

for e, d in zip(E, D):
  if len(e) > d:
    print(-1)
    exit()

CZ = [[] for _ in range(N)]
for i in range(N):
  c = uf.find(i)
  CZ[c].extend([i] * (D[i] - len(E[i])))

CZ1 = []
CZ2 = []

for cz in CZ:
  if len(cz) == 0: continue
  if len(cz) == 1:
    CZ1.append(cz)
  else:
    CZ2.append(cz)

#print(CZ1)
#print(CZ2)

ans = []

if len(CZ2) == 0:
  if len(CZ1) > 2:
    print(-1)
    exit()

  ans.append((
      CZ1[0][0],
      CZ1[1][0],
  ))

else:
  R = []
  p = None
  for i, cz in enumerate(CZ2):
    if p is not None:
      ans.append((p, cz[1]))
    else:
      R.append(cz[1])

    if i < len(CZ2) - 1:
      p = cz[0]
    else:
      R.append(cz[0])

    R.extend(cz[2:])

  if len(CZ1) != len(R):
    print(-1)
    exit()

  for cz, r in zip(CZ1, R):
    ans.append((cz[0], r))

if len(ans) != N - M - 1:
  print(-1)
  exit()

for x1, x2 in ans:
  print(x1 + 1, x2 + 1)
