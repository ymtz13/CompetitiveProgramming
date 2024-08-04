from heapq import heappop, heappush

N = int(input())
N2 = N + 2
N2sq = N2 * N2

S = ["_" * N2] + ["_{}_".format(input()) for _ in range(N)] + ["_" * N2]

INF = 1 << 60


def dijkstra(S, c, st, gl):
    sh, sw = st
    gh, gw = gl

    heap = [sh * N2 + sw]
    dist = [INF] * N2sq

    while heap:
        q = heappop(heap)
        d = q // N2sq
        hw = q % N2sq

        if dist[hw] < INF:
            continue
        dist[hw] = d

        h = hw // N2
        w = hw % N2

        s = S[h][w]
        if s == "_":
            continue

        dd = d if s == c else d + 1

        heappush(heap, dd * N2sq + hw - 1)
        heappush(heap, dd * N2sq + hw + 1)
        heappush(heap, dd * N2sq + hw - N2)
        heappush(heap, dd * N2sq + hw + N2)

    return dist[gh * N2 + gw]


dR = dijkstra(S, "R", (1, 1), (N, N))
dB = dijkstra(S, "B", (1, N), (N, 1))

print(dR + dB)
