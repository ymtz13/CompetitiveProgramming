from collections import deque

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
  A, B = map(int, input().split())
  E[A-1].append(B-1)
  E[B-1].append(A-1)

def bfs(root):
  queue = deque([(root, 0)])
  dist = [-1]*N

  while queue:
    q, d = queue.popleft()
    if dist[q] >= 0: continue
    dist[q] = d
    retval = q

    for e in E[q]:
      queue.append((e, d+1))
  
  return retval

v1 = bfs(0)
v2 = bfs(v1)
print(v1+1, v2+1)
