from collections import deque

N = int(input())
E = [[] for _ in range(N)]

for _ in range(N - 1):
  a, b = map(int, input().split())
  E[a - 1].append(b - 1)
  E[b - 1].append(a - 1)

visited = [False] * N
depth = [None] * N
queue = deque([(0, 0)])
while queue:
  q, d = queue.popleft()
  depth[q] = d

  for e in E[q]:
    if depth[e] is None: queue.append((e, d + 1))

Q0 = []
Q1 = []
for q, d in enumerate(depth):
  Q = Q1 if d % 2 else Q0
  Q.append(q)

if len(Q1) < len(Q0): Q0, Q1 = Q1, Q0

ans = [None] * N

N3 = N // 3
N1 = N3 + 1 if N % 3 > 0 else N3
N2 = N3 + 1 if N % 3 > 1 else N3

if len(Q0) <= N3:
  for q in Q0:
    ans[q] = 3
  for q, v in zip(Q1, [1] * N1 + [2] * N2 + [3] * N3):
    ans[q] = v

else:
  for q, v in zip(Q0, [1] * N1 + [3] * N3):
    ans[q] = v
  for q, v in zip(Q1, [2] * N2 + [3] * N3):
    ans[q] = v

X = [0] * 4
for q, a in enumerate(ans):
  ans[q] += X[a]
  X[a] += 3

print(' '.join(map(str, ans)))
