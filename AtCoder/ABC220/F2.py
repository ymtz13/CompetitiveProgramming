from collections import deque

N = int(input())
M = N * 2
E = [[] for _ in range(N)]
for i in range(N - 1):
  u, v = map(int, input().split())
  E[u - 1].append(v - 1)
  E[v - 1].append(u - 1)

P = [None] * N
V = []

stack = deque([(0, None)])
while stack:
  i, p = stack.pop()
  P[i] = p
  V.append(i)

  for e in E[i]:
    if e != p: stack.append((e, i))

C = [None] * N
D = [None] * N

for i in reversed(V):
  c = d = 0
  for e in E[i]:
    if e == P[i]: continue
    c += C[e]
    d += D[e]
  d += c
  c += 1

  C[i] = c
  D[i] = d

ans = [None] * N
ans[0] = D[0]
for i in V[1:]:
  ans[i] = ans[P[i]] - C[i] * 2 + N

for a in ans:
  print(a)
