from heapq import heappop, heappush

H, W = map(int, input().split())
H2 = H + 2
W2 = W + 2
M = H2 * W2

A = []
A.append([-1] * W2)
A.extend([[-1] + list(map(int, input().split())) + [-1] for _ in range(H)])
A.append([-1] * W2)

INF = 1 << 60

M2 = M * M
dist = [INF] * M2

heap = [W2 + 1]

while heap:
    q = heappop(heap)

    d = q // M2
    q %= M2

    if dist[q] < INF:
        continue

    c = q // M
    hw = q % M
    h = hw // W2
    w = hw % W2

    if h == 0 or h == H + 1 or w == 0 or w == W + 1:
        dist[q] = -1
        continue

    dd = (c * 2 - 1) * A[h][w] + d
    dist[q] = dd

    if c == M - 1:
        continue

    # print((d, c, h, w, A[h][w]), dd)

    heappush(heap, dd * M2 + (c + 1) * M + hw - W2)
    heappush(heap, dd * M2 + (c + 1) * M + hw + W2)
    heappush(heap, dd * M2 + (c + 1) * M + hw - 1)
    heappush(heap, dd * M2 + (c + 1) * M + hw + 1)

ans = INF
for c in range(M):
    i = c * M + H * W2 + W
    ans = min(ans, dist[i])

print(ans)
