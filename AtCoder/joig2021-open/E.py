from heapq import heappop, heappush

N, M, L = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    E[A - 1].append((B - 1, C, 0))
    E[B - 1].append((A - 1, C, 1))

N2 = N * N
INF = 1 << 60
dist = [INF] * N2
heap = [0]

while heap:
    q = heappop(heap)

    d = q // N2
    q = q % N2
    if dist[q] < INF:
        continue
    dist[q] = d

    x = q // N
    q = q % N

    for e, c, t in E[q]:
        if x + t < N:
            heappush(heap, (d + c) * N2 + (x + t) * N + e)

for x in range(N):
    if dist[x * N + N - 1] <= L:
        print(x)
        exit()

print(-1)
