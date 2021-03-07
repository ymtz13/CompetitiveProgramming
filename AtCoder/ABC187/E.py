from collections import deque

N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N-1)]

E = [[] for _ in range(N)]
for A, B in AB:
  E[A-1].append(B-1)
  E[B-1].append(A-1)

D = [None]*N

queue = deque()
queue.append((0, 0))

while queue:
  i, d = queue.popleft()
  if D[i] is not None: continue
  D[i] = d

  for e in E[i]:
    queue.append((e, d+1))

X = [0]*N

Q = int(input())
for _ in range(Q):
  t, e, x = map(int, input().split())
  if t==1:
    a, b = AB[e-1]
  else:
    b, a = AB[e-1]
  
  if D[a-1]>D[b-1]:
    X[a-1] += x
  else:
    X[0] += x
    X[b-1] -= x

C = [None]*N

queue = deque()
queue.append((0, 0))

while queue:
  i, c = queue.popleft()
  if C[i] is not None: continue
  c += X[i]
  C[i] = c

  for e in E[i]:
    queue.append((e, c))

for c in C:
  print(c)
