from collections import deque
from heapq import heappop, heappush

N, M, K, S = map(int, input().split())
N1 = N + 1

P, Q = map(int, input().split())
C = [int(input()) for _ in range(K)]

E = [[] for _ in range(N1)]
for _ in range(M):
    A, B = map(int, input().split())
    E[A].append(B)
    E[B].append(A)

queue = deque(C)
dist = [-1] * (N1)
while queue:
    q = queue.popleft()
    d, q = q // N1, q % N1

    if dist[q] != -1:
        continue
    dist[q] = d

    for e in E[q]:
        queue.append((d + 1) * N1 + e)

D = [0] * N1
for i, d in enumerate(dist):
    if d == 0:
        D[i] = 2
    elif d <= S:
        D[i] = 1

D[N] = -1


heap = [1]
dist = [-1] * N1
while heap:
    q = heappop(heap)
    d, q = q // N1, q % N1

    if dist[q] != -1:
        continue
    dist[q] = d

    for e in E[q]:
        if D[e] == -1:
            heappush(heap, d * N1 + e)
        if D[e] == 0:
            heappush(heap, (d + P) * N1 + e)
        if D[e] == 1:
            heappush(heap, (d + Q) * N1 + e)

print(dist[-1])
