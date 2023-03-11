from collections import deque

N = int(input())
xyP = [tuple(map(int, input().split())) for _ in range(N)]
P = [p for _, _, p in xyP]
D = [[None] * N for _ in range(N)]

for i, (x1, y1, _) in enumerate(xyP):
  for j, (x2, y2, _) in enumerate(xyP):
    d = abs(x1 - x2) + abs(y1 - y2)
    D[i][j] = D[j][i] = d


def check(S):
  for st in range(N):
    visited = [False] * N
    queue = deque([st])
    while queue:
      q = queue.popleft()
      if visited[q]: continue
      visited[q] = True

      for e in range(N):
        d = D[q][e]
        if d > 0 and P[q] * S >= d: queue.append(e)

    if all(visited): return True

  return False


ok = 1 << 60
ng = 0

while ok - ng > 1:
  tgt = (ok + ng) // 2
  if check(tgt):
    ok = tgt
  else:
    ng = tgt

print(ok)
