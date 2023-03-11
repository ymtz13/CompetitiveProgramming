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


N = int(input())
E = [[] for _ in range(N)]
D = [0] * N
for _ in range(N):
  u, v = map(int, input().split())
  E[u - 1].append(v - 1)
  E[v - 1].append(u - 1)
  D[u - 1] += 1
  D[v - 1] += 1

uf = UF(N)

queue = deque([i for i, d in enumerate(D) if d == 1])
deleted = [False] * N
while queue:
  i = queue.popleft()
  deleted[i] = True

  for e in E[i]:
    uf.union(i, e)

    if D[e] > 0:
      D[e] -= 1
      if D[e] == 1: queue.append(e)

#print(deleted)
#for i in range(N):
#  print(i+1, uf.find(i), deleted[i])

Q = int(input())
ans = []
for _ in range(Q):
  x, y = map(int, input().split())
  ans.append('Yes' if uf.find(x - 1) == uf.find(y - 1) else 'No')

for a in ans:
  print(a)
