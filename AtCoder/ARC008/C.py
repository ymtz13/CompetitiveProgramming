from heapq import heappush, heappop

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

if N == 1:
  print(0)
  exit()

E = [[0] * N for _ in range(N)]
for ip1, (x1, y1, t1, _) in enumerate(P):
  for ip2, (x2, y2, _, r2) in enumerate(P):
    if ip1 == ip2: continue
    dx = x2 - x1
    dy = y2 - y1
    d2 = dx * dx + dy * dy

    v = min(t1, r2)

    E[ip1][ip2] = pow(d2 / (v * v), 0.5)

INF = 1 << 60
D = [INF] * N
D[0] = 0
heap = [(0, 0)]
while heap:
  d, q = heappop(heap)
  if D[q] < d: continue

  for i, t in enumerate(E[q]):
    if q == i: continue
    dd = d + t
    if dd < D[i]:
      D[i] = dd
      heappush(heap, (dd, i))

X = [d + v for d, v in zip(sorted(D[1:], reverse=True), range(N - 1))]
print(max(X))
