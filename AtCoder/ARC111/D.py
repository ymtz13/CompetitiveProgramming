N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
C = list(map(int, input().split()))

ans = [None] * M
E = [[] for _ in range(N)]
for i, (a, b) in enumerate(AB):
  a -= 1
  b -= 1

  if C[a] > C[b]:
    ans[i] = +1
    continue

  if C[a] < C[b]:
    ans[i] = -1
    continue

  E[a].append((b, i, +1))
  E[b].append((a, i, -1))

visited = [False] * N
for st in range(N):
  if visited[st]: continue

  stack = [(st, None, None)]
  while stack:
    q, i, d = stack.pop()
    if i is not None:
      if ans[i] is not None: continue
      ans[i] = d

    for e, ii, dd in E[q]:
      stack.append((e, ii, dd))

for a in ans:
  print('->' if a == +1 else '<-')
