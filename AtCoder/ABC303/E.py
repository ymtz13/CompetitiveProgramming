from collections import deque

N = int(input())

E = [[] for _ in range(N)]
D = [0] * N
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    D[u] += 1
    D[v] += 1
    E[u].append(v)
    E[v].append(u)

for st, d in enumerate(D):
    if d == 1:
        break

dist = [None] * N
queue = deque([(st, 0)])
while queue:
    q, d = queue.popleft()
    if dist[q] is not None:
        continue
    dist[q] = d

    for e in E[q]:
        queue.append((e, d + 1))

ans = []
for d, deg in zip(dist, D):
    if d % 3 == 1:
        ans.append(deg)

ans.sort()
print(*ans)
