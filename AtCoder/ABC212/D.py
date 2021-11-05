from heapq import heappush, heappop

Q = int(input())

S = 0
heap = []
for _ in range(Q):
  q = tuple(map(int, input().split()))
  t = q[0]

  if t == 1: heappush(heap, q[1] - S)
  if t == 2: S += q[1]
  if t == 3: print(heappop(heap) + S)

