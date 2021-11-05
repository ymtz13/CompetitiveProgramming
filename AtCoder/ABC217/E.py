from heapq import heappush, heappop
from collections import deque

Q = int(input())

heap = []
queue = deque([])

for _ in range(Q):
  q = input().split()
  t = int(q[0])

  if t==1:
    x = int(q[1])
    queue.append(x)
  
  if t==2:
    if heap:
      print(heappop(heap))
    else:
      print(queue.popleft())
  
  if t==3:
    for v in queue:
      heappush(heap, v)
    queue.clear()
