from collections import deque

mod = 998244353

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  U, V = map(int, input().split())
  E[U - 1].append(V - 1)
  E[V - 1].append(U - 1)

visited = [False] * N
ans = 1

for s in range(N):
  if visited[s]: continue

  queue = deque([s])
  n = m = 0
  while queue:
    q = queue.popleft()
    if visited[q]: continue
    visited[q] = True
    n += 1

    for e in E[q]:
      m += 1
      queue.append(e)

  if n * 2 == m:
    ans *= 2
    ans %= mod

  else:
    ans = 0

print(ans)
