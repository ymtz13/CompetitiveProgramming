from collections import deque

N = int(input())
D = list(map(int, input().split()))

E = [[] for _ in range(N)]
for _ in range(N - 1):
  u, v, w = map(int, input().split())
  E[u - 1].append((v - 1, w))
  E[v - 1].append((u - 1, w))

P = [None] * N
T = []
queue = deque([(0, None)])
while queue:
  q, p = queue.popleft()
  T.append(q)
  if p is not None: P[q] = p

  for e, _ in E[q]:
    if e == p: continue
    queue.append((e, q))

INF = 1 << 60

V0 = [-INF] * N
V1 = [-INF] * N
for q in reversed(T):
  C = []
  ss = 0
  for e, w in E[q]:
    if e == P[q]: continue
    s1 = V0[e] + w
    s0 = V1[e]

    ss += s0

    if s1 - s0 > 0: C.append(s1 - s0)

  C.sort(reverse=True)

  d = D[q]
  if d > 0:
    V0[q] = ss + sum(C[:d - 1])
  V1[q] = ss + sum(C[:d])

print(V1[0])
