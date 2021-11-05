from sys import setrecursionlimit
setrecursionlimit(100000)

class UF:
  def __init__(self, N):
    self.uf = [-1]*N
    self.n = N

  def find(self, x):
    if self.uf[x]<0: return x
    self.uf[x] = self.find(self.uf[x])
    return self.uf[x]

  def size(self, x):
    return -self.uf[self.find(x)]

  def union(self, x, y):
    x, y = self.find(x), self.find(y)
    if x==y: return
    if self.size(x) > self.size(y): x, y = y, x
    self.uf[y] += self.uf[x]
    self.uf[x] = y
    self.n -= 1

N, M = map(int, input().split())
E = [[] for _ in range(N)]
uf = UF(N)
for _ in range(M):
  A, B = map(int, input().split())
  E[A-1].append(B-1)
  E[B-1].append(A-1)
  uf.union(A-1, B-1)

C = [[] for _ in range(N)]
for x in range(N):
  C[uf.find(x)].append(x)

ans = 1
P = [None] * N
D = [[] for _ in range(N)]

def tree(i, p, X):
  if P[i] is not None: return
  X.append(i)
  P[i] = p
  for e in E[i]:
    tree(e, i, X)

def dfs(i, X):
  if i == len(X):
    return 1
  
  ok = {1,2,3}
  x = X[i]
  for e in E[x]:
    if Z[e] is not None: ok.discard(Z[e])
  
  retval = 0
  for cc in ok:
    Z[x] = cc
    retval += dfs(i+1, X)
  Z[x] = None
  
  return retval

Z = [None] * N

for c in C:
  if len(c)==0: continue

  X = []
  tree(c[0], -1, X)

  ans *= dfs(0, X)

print(ans)
