from collections import deque

N, M = map(int, input().split())
S = input()
CA = [0] * N
CB = [0] * N
E = [[] for _ in range(N)]
for _ in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  E[u].append(v)
  E[v].append(u)

  if S[u] == 'A': CA[v] += 1
  if S[u] == 'B': CB[v] += 1
  if S[v] == 'A': CA[u] += 1
  if S[v] == 'B': CB[u] += 1

queue = deque([i for i in range(N) if CA[i] == 0 or CB[i] == 0])
visited = [False] * N
while queue:
  q = queue.popleft()
  if visited[q]: continue
  visited[q] = True

  C = CA if S[q] == 'A' else CB
  for e in E[q]:
    C[e] -= 1
    if C[e] == 0: queue.append(e)

print('No' if all(visited) else 'Yes')
