from heapq import heappush, heappop

N, M = map(int, input().split())
C = [[] for _ in range(N)]
D = [0] * N
for _ in range(M):
  A, B = map(int, input().split())
  C[A - 1].append(B - 1)
  D[B - 1] += 1

heap = []
for i, d in enumerate(D):
  if d == 0: heappush(heap, i)

ans = []
for _ in range(N):
  if not heap:
    print(-1)
    exit()

  a = heappop(heap)
  ans.append(a)

  for b in C[a]:
    D[b] -= 1
    if D[b] == 0:
      heappush(heap, b)

print(' '.join(map(str, [a + 1 for a in ans])))
