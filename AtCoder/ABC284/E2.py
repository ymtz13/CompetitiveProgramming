from collections import deque

X = 1000000

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  u, v = map(int, input().split())
  E[u - 1].append(v - 1)
  E[v - 1].append(u - 1)

ans = 0
V = [False] * N

stack = deque([(0, True)])

while stack and ans < X:
  q, f = stack.pop()
  if f:
    V[q] = True
    stack.append((q, False))
    ans += 1

    for e in E[q]:
      if V[e]: continue
      stack.append((e, True))

  else:
    V[q] = False

print(ans)
