from heapq import heappush, heappop
from collections import deque

N, M = map(int, input().split())
P = list(map(int, input().split()))
L = list(map(int, input().split()))
D = list(map(int, input().split()))

P.sort()

LD = deque(sorted(zip(L, D)))

ans = 0
heap = []
for p in P:
    while LD and LD[0][0] <= p:
        l, d = LD.popleft()
        heappush(heap, -d)

    ans += p
    if heap:
        ans += heappop(heap)

print(ans)
