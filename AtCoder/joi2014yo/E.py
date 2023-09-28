from collections import deque
from heapq import heappop, heappush

N, K = map(int, input().split())
N1 = N + 1

CR = [None] + [tuple(map(int, input().split())) for _ in range(N)]


E = [[] for _ in range(N1)]
for _ in range(K):
    A, B = map(int, input().split())
    E[A].append(B)
    E[B].append(A)

D = [[1 << 60] * (N1) for _ in range(N1)]

for st in range(1, N1):
    queue = deque([st])
    visited = [False] * N1

    C, R = CR[st]

    while queue:
        q = queue.popleft()
        d, q = q // N1, q % N1

        if visited[q]:
            continue
        visited[q] = True

        if 0 < d <= R:
            D[st][q] = C

        if d >= R:
            continue

        for e in E[q]:
            queue.append((d + 1) * N1 + e)


heap = [1]
dist = [-1] * N1
INF = 1 << 60

while heap:
    q = heappop(heap)
    d, q = q // N1, q % N1

    if dist[q] != -1:
        continue
    dist[q] = d

    for e, dd in enumerate(D[q]):
        if dd < INF:
            heappush(heap, (d + dd) * N1 + e)

print(dist[-1])
