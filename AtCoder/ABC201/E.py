from collections import deque

N = int(input())

E = [[] for _ in range(N)]
for _ in range(N-1):
  u, v, w = map(int, input().split())
  E[u-1].append((v-1, w))
  E[v-1].append((u-1, w))

X = [0]*N
queue = deque([(0, None, 0)])
while queue:
  i, p, x = queue.popleft()

  X[i] = x
  for v, w in E[i]:
    if v != p:
      queue.append((v, i, x ^ w))

ans = 0
mod = 10**9+7
for d in range(60):
  b = 1<<d

  n0 = 0
  for x in X:
    if x&b ==0 : n0+=1

  ans += n0*(N-n0)*b%mod
  ans %= mod

print(ans)
