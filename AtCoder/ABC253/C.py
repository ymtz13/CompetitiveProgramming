from heapq import heappush, heappop
from collections import defaultdict

Q = int(input())
C = defaultdict(int)

minheap = []
maxheap = []

ans = []

for _ in range(Q):
  q = input().split()

  if q[0] == '1':
    x = int(q[1])

    C[x] += 1
    heappush(minheap, (+x, -C[x]))
    heappush(maxheap, (-x, -C[x]))

  if q[0] == '2':
    x, c = map(int, q[1:])
    C[x] -= min(c, C[x])

  if q[0] == '3':
    while minheap:
      x, c = minheap[0]
      if -c <= C[x]: break
      heappop(minheap)

    while maxheap:
      x, c = maxheap[0]
      if -c <= C[-x]: break
      heappop(maxheap)

    xmin = +minheap[0][0]
    xmax = -maxheap[0][0]
    ans.append(xmax - xmin)

for a in ans:
  print(a)
