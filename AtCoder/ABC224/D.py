from collections import deque

M = int(input())
E = [[] for _ in range(10)]
for _ in range(M):
  u, v = map(int, input().split())
  E[u].append(v)
  E[v].append(u)

P = tuple(map(int, input().split()))
X = ['0'] * 10
for i, p in enumerate(P, 1):
  X[p] = str(i)

dist = {}

for p, x in enumerate(X):
  if x == '0': p0 = p

queue = deque([(X, p0, 0)])
while queue:
  x, p0, d = queue.popleft()
  key = int(''.join(x))
  if key in dist: continue
  dist[key] = d

  for pe in E[p0]:
    xe = x[pe]

    x2 = x[:]
    x2[pe] = '0'
    x2[p0] = xe
    queue.append((x2, pe, d + 1))

anskey = 123456780
print(dist[anskey] if anskey in dist else -1)
