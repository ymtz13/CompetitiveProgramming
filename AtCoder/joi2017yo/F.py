from heapq import heappop, heappush

N, M, X = map(int, input().split())
T = [int(input()) for _ in range(N)]
E = [[] for _ in range(M)]
for _ in range(M):
    A, B, D = map(int, input().split())
    E[A - 1].append((B - 1, D))
    E[B - 1].append((A - 1, D))

INF = 1 << 60

Z = X * 2 + 1
NZ = N * Z

dist = [INF] * NZ
heap = [0]

while heap:
    q = heappop(heap)

    d = q // NZ
    it = q % NZ

    if dist[it] < INF:
        continue
    dist[it] = d

    i = it // Z
    t = it % Z
    # print(">", i + 1, t, d)

    for j, dd in E[i]:
        tj = T[j]
        if tj == 0:
            tt = 0
        if tj == 1:
            if t <= X:
                tt = min(X, t + dd)
            else:
                tt = max(X, t - dd)
        if tj == 2:
            tt = 2 * X

        if t < X and tj == 2 and X - t > dd:
            continue
        if t > X and tj == 0 and t - X > dd:
            continue

        heappush(heap, (d + dd) * NZ + j * Z + tt)

print(min(dist[-Z:]))
