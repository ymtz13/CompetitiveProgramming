from heapq import heappop, heappush

N, A, B, C = map(int, input().split())
D = [tuple(map(int, input().split())) for _ in range(N)]

N2 = N * 2

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

    i = q // 2
    t = q % 2

    if t == 0:
        heappush(heap, d * N2 + i * 2 + 1)
        for j, dij in enumerate(D[i]):
            if i == j:
                continue
            dd = d + dij * A
            heappush(heap, dd * N2 + j * 2)
    else:
        for j, dij in enumerate(D[i]):
            if i == j:
                continue
            dd = d + dij * B + C
            heappush(heap, dd * N2 + j * 2 + 1)

print(dist[-1])
