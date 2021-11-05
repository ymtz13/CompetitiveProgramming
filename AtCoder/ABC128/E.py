from heapq import heappush, heappop

N, Q = map(int, input().split())
E = []

for i in range(N):
  S, T, X = map(int, input().split())
  E.append((S - X - 0.5, 1, X, i))
  E.append((T - X - 0.5, 2, X, i))

for _ in range(Q):
  D = int(input())
  E.append((D, 0, None, None))

E.sort()

heap = []
deleted = [False] * N

M = 10**6

for _, type, x, i in E:
  if type == 0:
    while heap and deleted[heap[0] % M]:
      heappop(heap)

    if heap:
      print(heap[0] // M)
    else:
      print(-1)

  if type == 1:
    heappush(heap, x * M + i)

  if type == 2:
    deleted[i] = True
