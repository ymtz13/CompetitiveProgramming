from heapq import heappop, heappush

N, K = map(int, input().split())
P = list(map(int, input().split()))

heap = []

for i, p in enumerate(P):
    for j, q in enumerate(P[i + K :], i + K):
        if q < p:
            heappush(heap, (p - q, i, j, p, q))

# print(heap)

ans = []
done = [False] * (N * N)
while heap:
    _, i, j, p, q = heappop(heap)
    if P[i] != p or P[j] != q or done[i * N + j]:
        continue
    ans.append((i + 1, j + 1))
    done[i * N + j] = True
    p, q = q, p
    P[i] = p
    P[j] = q
    for jj, qq in enumerate(P[i + K :], i + K):
        if qq < p:
            heappush(heap, (p - qq, i, jj, p, qq))
    for ii, pp in enumerate(P[: j - K + 1]):
        if q < pp:
            heappush(heap, (pp - q, ii, j, pp, q))


print(len(ans))
for i, j in ans:
    print(i, j)
