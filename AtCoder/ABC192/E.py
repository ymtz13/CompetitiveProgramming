from heapq import heappush, heappop

N, M, X, Y = map(int, input().split())
E = [[] for _ in range(N)]
for m in range(M):
  A, B, T, K = map(int, input().split())
  E[A-1].append((B-1, T, K))
  E[B-1].append((A-1, T, K))

queue = [(0, X-1)]
time = [None] * N
while queue:
  now, q = heappop(queue)
  if time[q] is not None: continue
  time[q] = now

  for e, t, k in E[q]:
    if time[e] is None:
      departure = now if now%k==0 else now + k - now%k
      arrival = departure + t
      heappush(queue, (arrival, e))

ans = time[Y-1]
print(ans if ans else -1)
