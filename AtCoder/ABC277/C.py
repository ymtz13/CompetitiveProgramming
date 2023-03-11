from collections import defaultdict, deque

N = int(input())
E = defaultdict(list)
for _ in range(N):
  A, B = map(int, input().split())
  E[A].append(B)
  E[B].append(A)

visited = set()
queue = deque([1])

while queue:
  q = queue.popleft()
  if q in visited: continue
  visited.add(q)

  for e in E[q]:
    queue.append(e)

print(max(visited))
