from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
T = []

for _ in range(M):
  U, V = map(int, input().split())
  if U == 0:
    T.append(V - 1)
  else:
    E[U - 1].append(V - 1)
    E[V - 1].append(U - 1)


def bfs(st):
  queue = deque([(st, 0)])
  dist = [INF] * N
  while queue:
    q, d = queue.popleft()
    if dist[q] < INF: continue
    dist[q] = d

    for e in E[q]:
      queue.append((e, d + 1))

  return dist


INF = 1 << 60

D1 = bfs(0)
DN = bfs(N - 1)

T1 = min([D1[i] for i in T] + [INF]) + 1
TN = min([DN[i] for i in T] + [INF]) + 1

ans = []
for i in range(N):
  a = min(DN[0], min(D1[i], T1) + min(DN[i], TN))k
  ans.append(a if a < INF else -1)

print(' '.join(map(str, ans)))
