from collections import deque

N = int(input())
P = list(map(int, input().split()))

C = [[] for _ in range(N)]
for i, p in enumerate(P, 1):
  C[p - 1].append(i)

Q = int(input())
X = [[] for _ in range(N)]
for q in range(Q):
  U, D = map(int, input().split())
  X[U - 1].append((q, D))

D = [0] * N
ans = [None] * Q

T = [[] for _ in range(N)]

stack = deque([(0, 0, 0)])
while stack:
  i, depth, t = stack.pop()

  if t == 0:
    for _, d in X[i]:
      T[i].append(D[d])

    D[depth] += 1

    stack.append((i, depth, 1))
    for c in C[i]:
      stack.append((c, depth + 1, 0))

  else:
    for t, (q, d) in zip(T[i], X[i]):
      ans[q] = D[d] - t

for a in ans:
  print(a)
