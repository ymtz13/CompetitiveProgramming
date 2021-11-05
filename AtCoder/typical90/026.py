from collections import deque

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
  A, B = map(int, input().split())
  E[A-1].append(B-1)
  E[B-1].append(A-1)

queue = deque([(0, 0)])
depth = [None]*N
odd = []
even = []
while queue:
  q, d =  queue.popleft()
  if depth[q] is not None: continue
  depth[q] = d
  if d%2==0: even.append(q+1)
  else     : odd .append(q+1)

  for e in E[q]:
    queue.append((e, d+1))

arr = odd if len(odd)>=N//2 else even
print(' '.join(map(str, arr[:N//2])))
