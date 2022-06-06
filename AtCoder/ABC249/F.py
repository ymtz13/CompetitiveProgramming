from heapq import heappop, heappush

N, K = map(int, input().split())
OP = [(1, 0)] + [tuple(map(int, input().split())) for _ in range(N)]

heap = []
Sall = 0
Sheap = 0

ans = -(1 << 60)

for t, y in reversed(OP):
  if t == 1:
    if K < 0: break

    while len(heap) > K:
      Sheap -= -heappop(heap)

    ans = max(ans, y + Sall - Sheap)
    K -= 1

  else:
    Sall += y
    if y < 0:
      Sheap += y
      heappush(heap, -y)

print(ans)
