from collections import deque


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


N, M, Q = map(int, input().split())

E = [[] for _ in range(N)]
EE = []
for _ in range(M):
  A, B, C = map(int, input().split())
  A -= 1
  B -= 1

  E[A].append((B, +C))
  E[B].append((A, -C))

  EE.append((A, B, C))

uf = UF(N)
potential = [None] * N

for root in range(N):
  if potential[root] is not None: continue

  queue = deque([(root, 0)])
  while queue:
    q, p = queue.popleft()
    if potential[q] is not None: continue
    potential[q] = p

    for e, c in E[q]:
      queue.append((e, p + c))
      uf.union(q, e)

isINF = [False] * N

for a, b, c in EE:
  if potential[b] - potential[a] != c:
    isINF[uf.find(a)] = True

ans = []
for _ in range(Q):
  X, Y = map(int, input().split())
  X -= 1
  Y -= 1

  if uf.find(X) != uf.find(Y):
    ans.append('nan')

  elif isINF[uf.find(X)]:
    ans.append('inf')

  else:
    ans.append(potential[Y] - potential[X])

for a in ans:
  print(a)
