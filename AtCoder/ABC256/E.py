N = int(input())
X = list(map(int, input().split()))
C = list(map(int, input().split()))

visited = [False] * N
loop = [False] * N
ans = 0

for st in range(N):
  if visited[st]: continue

  path = set()
  p = st
  while not visited[p]:
    visited[p] = True
    path.add(p)
    p = X[p] - 1

  if p not in path: continue

  q = p
  c = 1 << 60
  while True:
    c = min(c, C[q])
    q = X[q] - 1
    if q == p: break
  
  ans += c

print(ans)
