from heapq import heappop, heappush

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    l, d, k, c, A, B = map(int, input().split())
    E[B - 1].append((A - 1, l, d, k, c))

INF = 1 << 60
time = [None] * N

heap = [(-INF) * N + (N - 1)]
while heap:
    v = heappop(heap)
    t = -(v // N)
    q = v % N

    if time[q] is not None:
        continue
    time[q] = t

    for e, l, d, k, c in E[q]:
        x = (t - c - l) // d
        if x < 0:
            continue
        x = min(x, k - 1)
        tt = l + x * d
        heappush(heap, (-tt) * N + e)

for t in time[:-1]:
    print(t if t is not None else "Unreachable")
