from collections import deque, defaultdict

N = int(input())
E = [[] for _ in range(N)]

for _ in range(N - 1):
  U, V = map(int, input().split())
  E[U - 1].append(V - 1)
  E[V - 1].append(U - 1)

if N == 2:
  print(1)
  exit()

depth0 = [None] * N
queue = deque([0])
while queue:
  dq = queue.popleft()
  d, q = dq // N, dq % N
  depth0[q] = d

  for e in E[q]:
    if depth0[e] is None: queue.append((d + 1) * N + e)

#print(depth0)
md0 = max(depth0)
for q, d in enumerate(depth0):
  if d == md0: s1 = q

#print(q)

depth1 = [None] * N
queue = deque([(0, s1, -1)])
come_from = [None] * N
while queue:
  d, q, c = queue.popleft()
  depth1[q] = d
  come_from[q] = c

  for e in E[q]:
    if depth1[e] is None: queue.append((d + 1, e, q))

#print(depth1)
#print(come_from)

D = max(depth1)
for q, d in enumerate(depth1):
  if d == D: t = q

path = []
while t >= 0:
  path.append(t)
  t = come_from[t]

#print(path)

root = path[D // 2]

depth = [None] * N
depth[root] = 0
queue = deque([(1, e, e) for e in E[root]])

Z0 = defaultdict(int)
Z1 = defaultdict(int)

while queue:
  d, q, c = queue.popleft()
  depth[q] = d
  if d == D // 2: Z0[c] += 1
  if d == D // 2 + 1: Z1[c] += 1

  for e in E[q]:
    if depth[e] is None: queue.append((d + 1, e, c))

#print(Z1.items())

########
X1 = [z1 for c, z1 in Z1.items()]
X0 = [z0 for c, z0 in Z0.items() if Z1[c] == 0]
########

#print(X0, X1)

mod = 998244353

if D % 2 == 0:
  ans = 1
  for x in X0:
    ans *= x + 1
    ans %= mod
  ans -= sum(X0) + 1
  ans %= mod

else:
  ans = sum(X0) * sum(X1)
  ans %= mod

print(ans)
