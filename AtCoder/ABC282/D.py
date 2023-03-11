from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]

for _ in range(M):
  u, v = map(int, input().split())
  E[u - 1].append(v - 1)
  E[v - 1].append(u - 1)

ans = N * (N - 1) // 2 - M

d = [None] * N
for st in range(N):
  if d[st] is not None: continue

  cnt = [0, 0]
  queue = deque([(st, 0)])

  while queue:
    q, x = queue.popleft()
    if d[q] is not None:
      if d[q] != x:
        print(0)
        exit()
      continue

    d[q] = x
    cnt[x] += 1

    for e in E[q]:
      queue.append((e, 1 - x))

  for c in cnt:
    ans -= c * (c - 1) // 2

print(ans)
