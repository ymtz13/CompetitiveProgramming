from collections import deque

mod = 10**9 + 7
INF = 10**10
N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A-1].append(B-1)
  E[B-1].append(A-1)

D = [INF]*N
queue = deque([(0, 0)])

while queue:
  q, d = queue.popleft()
  if D[q] < INF: continue
  D[q] = d

  for e in E[q]:
    queue.append((e, d+1))

if D[-1] is None:
  print(0)
  exit()

X = sorted([(d, i) for i, d in enumerate(D)])

A = [0]*N
A[0] += 1
for d, i in X[1:]:
  for e in E[i]:
    if D[e] == d-1:
      A[i] += A[e]
      A[i] %= mod

print(A[-1])
