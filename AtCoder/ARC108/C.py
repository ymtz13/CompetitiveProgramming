N, M = map(int, input().split())
E = [[] for _ in range(N+1)]
for _ in range(M):
  u, v, c = map(int, input().split())
  E[u].append((v, c))
  E[v].append((u, c))


T = [[] for _ in range(N+1)]
queue = [(1, 0, 0)]
iq = 0
visited = [False] * (N+1)
used = [False] * (N+1)
while iq < len(queue):
  q, p, c = queue[iq]
  iq += 1

  if visited[q]: continue
  visited[q] = True
  used[c] = True

  T[p].append((q, c))

  for e, ec in E[q]:
    if visited[e]: continue
    queue.append((e, q, ec))

for c in range(1, N+1):
  if not used[c]:
    nc = c
    break

#print(T)
#print(nc)

queue = [(1, nc)]
iq = 0
ans = [None] * (N+1)
while iq < len(queue):
  q, c = queue[iq]
  iq += 1

  ans[q] = c
  for t, tc in T[q]:
    queue.append((t, tc if c!=tc else nc))

for a in ans[1:]:
  print(a)
