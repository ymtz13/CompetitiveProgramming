from collections import deque

N = int(input())
E = [[] for _ in range(N - 1)]
for _ in range(N - 1):
  A, B = map(int, input().split())
  E[A - 1].append(B - 1)
  E[B - 1].append(A - 1)

queue = deque([(0, 0)])
depth = [None] * N
while queue:
  q, d = queue.popleft()
  depth[q] = d

  for e in E[q]:
    if depth[e] is not None: continue
    queue.append((e, d + 1))

maxD = max(depth)
for i in range(N):
  if depth[i] == maxD:
    root = i
    break

queue = deque([(root, -1)])
parent = [None] * N
while queue:
  q, p = queue.popleft()
  parent[q] = p

  for e in E[q]:
    if parent[e] is not None: continue
    queue.append((e, q))

last = e
L = [last]
while parent[last] != -1:
  last = parent[last]
  L.append(last)

ans = []
Q = int(input())
for _ in range(Q):
  U, K = map(int, input().split())

for a in ans:
  print(a)
