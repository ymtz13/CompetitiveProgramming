from collections import deque

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    E[u].append(v)
    E[v].append(u)


queue = deque([(0, None)])
visited = [False] * N
parent = [None] * N
D = []
while queue:
    q, p = queue.popleft()
    if visited[q]:
        continue
    visited[q] = True
    parent[q] = p
    D.append(q)

    for e in E[q]:
        if e == p:
            continue
        queue.append((e, q))

V = [None] * N
for q in reversed(D):
    p = parent[q]
    C = []
    for e in E[q]:
        if e == p:
            continue
        C.append(V[e])

    C.sort()
    V[q] = 1 + sum(C)

C = []
for e in E[0]:
    C.append(V[e])
C.sort()

ans = 1 + sum(C[:-1])
print(ans)
