from collections import deque

N, Q = map(int, input().split())
E = [[] for _ in range(N + 1)]
for _ in range(Q):
  l, r = map(int, input().split())
  E[l - 1].append(r)
  E[r].append(l - 1)

queue = deque([0])
visited = [False] * (N + 1)

while queue:
  q = queue.popleft()
  if visited[q]: continue
  visited[q] = True

  for e in E[q]:
    queue.append(e)

print('Yes' if visited[-1] else 'No')
