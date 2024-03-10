from collections import deque

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    E[x - 1].append(y - 1)
    E[y - 1].append(x - 1)

P = [None] * N
queue = deque([(0, -1)])
A = []
while queue:
    q, p = queue.popleft()
    if P[q] is not None:
        continue
    P[q] = p
    A.append(q)

    for e in E[q]:
        queue.append((e, q))

V = [0] * N
for a in reversed(A):
    v = 0
    for e in E[a]:
        if e != P[a]:
            v ^= 1 + V[e]
    V[a] = v

print("Alice" if V[0] else "Bob")
