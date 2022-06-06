from collections import deque

N = int(input())
A = list(map(int, input().split()))

queue = deque()
for a in A:
  if len(queue) > 0 and queue[-1][0] == a:
    s = queue[-1][1] + 1
    queue.append((a, s))

    if s == a:
      for _ in range(s):
        queue.pop()
  
  else:
    queue.append((a, 1))

  print(len(queue))
