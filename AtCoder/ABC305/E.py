from heapq import heappop, heappush

N, M, K = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

heap = []
for _ in range(K):
    p, h = map(int, input().split())
    heappush(heap, -((h + 1) * N + p - 1))

level = [0] * N
while heap:
    v = -heappop(heap)
    p = v % N
    h = v // N

    if h <= level[p]:
        continue
    level[p] = h

    if h > 1:
        hh = (h - 1) * N
        for e in E[p]:
            heappush(heap, -(hh + e))

ans = [i for i, l in enumerate(level, 1) if l]
print(len(ans))
print(*ans)
