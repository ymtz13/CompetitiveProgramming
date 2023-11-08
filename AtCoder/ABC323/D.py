from collections import defaultdict
from heapq import heappop, heappush

N = int(input())
D = defaultdict(int)
heap = []

for _ in range(N):
    S, C = map(int, input().split())
    D[S] = C
    heappush(heap, S)

ans = 0
while heap:
    v = heappop(heap)

    d = D[v]
    D[v] = 0
    D[v * 2] += d // 2
    ans += d % 2

    if D[v * 2]:
        heappush(heap, v * 2)


print(ans)
