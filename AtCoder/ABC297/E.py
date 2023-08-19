from heapq import heappop, heappush

N, K = map(int, input().split())
A = set(map(int, input().split()))

heap = [0]
visited = set()

while len(visited) <= K:
    q = heappop(heap)
    if q in visited:
        continue
    visited.add(q)

    for a in A:
        heappush(heap, q + a)

d = sorted(list(visited))
print(d[K])
