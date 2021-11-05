from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A-1].append(B-1)

ans = 0
for s in range(N):
  visited = [False]*N
  queue = deque([s])
  while queue:
    q = queue.popleft()
    if visited[q]: continue
    visited[q] = True
    ans += 1

    for e in E[q]:
      if not visited[e]: queue.append(e)

print(ans)

