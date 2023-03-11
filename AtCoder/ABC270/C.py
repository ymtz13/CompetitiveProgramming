from collections import deque

N, X, Y = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N - 1):
  U, V = map(int, input().split())
  E[U - 1].append(V - 1)
  E[V - 1].append(U - 1)

queue = deque([(Y - 1, -1)])
parent = [None] * N

while queue:
  q, p = queue.popleft()
  if parent[q] is not None: continue
  parent[q] = p

  for e in E[q]:
    if e != q: queue.append((e, q))

ans = []
q = X - 1
while q != -1:
  ans.append(q + 1)
  q = parent[q]

print(' '.join(map(str, ans)))
