from heapq import heappop, heappush

N, M = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(N)]

N2 = N * N

INF = 1 << 60
edges = [[INF] * N for _ in range(N)]
cost = [INF] * N2
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a][b] = edges[b][a] = c
    cost[a * N + b] = cost[b * N + a] = c

E = [[] for _ in range(N * N)]

for s in range(N):
    for t in range(N):
        if s == t:
            continue
        for u in range(N):
            if s == u or t == u:
                continue

            xs, ys = P[s]
            xt, yt = P[t]
            xu, yu = P[u]

            dx1 = xt - xs
            dy1 = yt - ys
            dx2 = xu - xt
            dy2 = yu - yt

            if dx1 * dx2 + dy1 * dy2 < 0:
                continue

            p = s * N + t
            q = t * N + u

            E[p].append(q)


heap = []
for i in range(1, N):
    heappush(heap, cost[i] * N2 + i)

dist = [-1] * N2

while heap:
    q = heappop(heap)
    c = q // N2
    q = q % N2

    if dist[q] != -1:
        continue
    dist[q] = c

    for e in E[q]:
        heappush(heap, (c + cost[e]) * N2 + e)

ans = INF
for i in range(N):
    if dist[i * N + 1] != -1:
        ans = min(ans, dist[i * N + 1])

print(ans if ans < INF else -1)
