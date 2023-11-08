from collections import defaultdict, deque
from heapq import heappop, heappush

N = int(input())
TD = [tuple(map(int, input().split())) for _ in range(N)]


D = defaultdict(list)
for t, d in TD:
    D[t].append(t + d)

TV = list(D.items())
TV.sort()
TV = deque(TV)

c = 0
heap = []
ans = 0
while TV or heap:
    if TV and (not heap or TV[0][0] == c):
        T, V = TV.popleft()
        c = T
        for v in V:
            heappush(heap, v)

    if heap:
        v = heappop(heap)
        if c <= v:
            ans += 1
            c += 1

print(ans)
exit()
