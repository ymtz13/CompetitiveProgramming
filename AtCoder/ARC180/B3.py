from heapq import heappop, heappush

N, K = map(int, input().split())
P = [p - 1 for p in list(map(int, input().split()))]

N2 = N * N
N3 = N * N2
N4 = N * N3

heap = []

for i, p in enumerate(P):
    for j, q in enumerate(P[i + K :], i + K):
        if q < p:
            d = p - q
            heappush(heap, d * N4 + i * N3 + j * N2 + p * N + q)

# print(heap)

ans = []
done = [False] * (N * N)
while heap:
    v = heappop(heap) % N4
    i = v // N3
    jpq = v % N3
    j = jpq // N2
    pq = jpq % N2
    p = pq // N
    q = pq % N

    if P[i] != p or P[j] != q or done[i * N + j]:
        continue
    ans.append((i + 1, j + 1))
    done[i * N + j] = True
    p, q = q, p
    P[i] = p
    P[j] = q
    for jj, qq in enumerate(P[i + K :], i + K):
        key = i * N + jj
        if not done[key] and qq < p:
            d = p - qq
            heappush(heap, d * N4 + i * N3 + jj * N2 + p * N + qq)
    for ii, pp in enumerate(P[: j - K + 1]):
        key = ii * N + j
        if not done[key] and q < pp:
            d = pp - q
            heappush(heap, d * N4 + ii * N3 + j * N2 + pp * N + q)


print(len(ans))
for i, j in ans:
    print(i, j)
