from heapq import heappop, heappush
from collections import deque

N, M = map(int, input().split())
TT = [[], [], []]

for _ in range(N):
    T, X = map(int, input().split())
    TT[T].append(X)

T0, T1, T2 = TT

heap = []
s = 0
for v in T0:
    heappush(heap, v)
    s += v

while len(heap) > M:
    s -= heappop(heap)

T1.sort(reverse=True)
T2.sort(reverse=True)
T1 = deque(T1)

ans = s

for t2 in T2:
    M -= 1
    if M == 0:
        break

    for _ in range(t2):
        if T1:
            v = T1.popleft()
            heappush(heap, v)
            s += v
        else:
            break

    while len(heap) > M:
        s -= heappop(heap)

    ans = max(ans, s)


print(ans)
