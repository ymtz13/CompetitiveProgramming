from heapq import heappop, heappush

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = [0] * N

E = [[] for _ in range(N)]
for _ in range(M):
  U, V = map(int, input().split())
  U -= 1
  V -= 1

  E[U].append(V)
  E[V].append(U)

  C[U] += A[V]
  C[V] += A[U]

queue = []
for i, c in enumerate(C):
  heappush(queue, (c, i))

deleted = [False] * N
ans = 0

while queue:
  c, i = heappop(queue)
  if deleted[i]: continue
  deleted[i] = True
  ans = max(ans, c)

  for e in E[i]:
    C[e] -= A[i]
    heappush(queue, (C[e], e))

print(ans)
