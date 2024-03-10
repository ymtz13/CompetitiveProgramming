from heapq import heappop, heappush

N = int(input())
E = [None] + [tuple(map(int, input().split())) for _ in range(N - 1)]

N1 = N + 1
heap = [1]
dist = [-1] * N1

while heap:
    q = heappop(heap)
    d, q = q // N1, q % N1

    if dist[q] != -1:
        continue
    dist[q] = d

    if q == N:
        break

    a, b, x = E[q]
    heappush(heap, (d + a) * N1 + (q + 1))
    heappush(heap, (d + b) * N1 + x)

print(dist[-1])
