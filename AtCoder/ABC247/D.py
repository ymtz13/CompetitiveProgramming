from collections import deque

Q = int(input())
queue = deque()

for _ in range(Q):
  q = tuple(map(int, input().split()))
  if q[0] == 1:
    queue.append(q[1:])

  else:
    _, c = q
    s = 0
    while c > 0:
      x, n = queue.popleft()
      z = min(c, n)
      c -= z
      s += x * z
      if z < n:
        queue.appendleft((x, n - z))

    print(s)
