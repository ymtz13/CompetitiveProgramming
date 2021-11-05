from heapq import heappush, heappop

N, K = map(int, input().split())
Q = []
for _ in range(N):
  A, B = map(int, input().split())
  heappush(Q, (-B, -1, -(A-B)))

ans = 0
for _ in range(K):
  B, t, A = heappop(Q)
  ans += -B
  if t==-1: heappush(Q, (A, 0, 0))

print(ans)
