from collections import defaultdict
from heapq import heappop, heappush

N = int(input())

Dr = defaultdict(int)
Dc = defaultdict(int)

Dp = defaultdict(int)

P = [tuple(map(int, input().split())) for _ in range(N)]

for r, c, x in P:
    Dr[r] += x
    Dc[c] += x

    Dp[(r, c)] = x

ans = 0
for r, c, x in P:
    a = Dr[r] + Dc[c] - x
    ans = max(ans, a)

Lr = list(Dr.items())
Lc = list(Dc.items())

Lr.sort(key=lambda x: -x[1])
Lc.sort(key=lambda x: -x[1])

heap = [(-(Lr[0][1] + Lc[0][1]), 0, 0)]
visited = set()
for _ in range(N + 10):
    # print(heap)
    if not heap:
        break

    v, ir, ic = heappop(heap)
    key = (ir, ic)
    if key in visited:
        continue
    visited.add(key)

    if ic == len(Lc):
        continue

    r, vr = Lr[ir]
    c, vc = Lc[ic]
    ans = max(ans, vr + vc - Dp[(r, c)])

    if ir + 1 < len(Lr):
        vr1 = Lr[ir + 1][1]
        heappush(heap, (-(vr1 + vc), ir + 1, ic))

    if ic + 1 < len(Lc):
        vc1 = Lc[ic + 1][1]
        heappush(heap, (-(vr + vc1), ir, ic + 1))


print(ans)


# 2 9
# 8
#   3
