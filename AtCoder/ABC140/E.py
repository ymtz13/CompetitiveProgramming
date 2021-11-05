from heapq import heappop, heappush

N = int(input())
P = list(map(int, input().split()))

R1 = [N] * N
R2 = [N] * N
L1 = [-1] * N
L2 = [-1] * N

heap1 = []
heap2 = []
for i, p in enumerate(P):
  while heap2 and heap2[0][0] < p:
    q, j = heappop(heap2)
    R2[j] = i

  while heap1 and heap1[0][0] < p:
    q, j = heappop(heap1)
    R1[j] = i
    heappush(heap2, (q, j))

  heappush(heap1, (p, i))

heap1 = []
heap2 = []
for i, p in enumerate(P[::-1]):
  i = N - 1 - i
  while heap2 and heap2[0][0] < p:
    q, j = heappop(heap2)
    L2[j] = i

  while heap1 and heap1[0][0] < p:
    q, j = heappop(heap1)
    L1[j] = i
    heappush(heap2, (q, j))

  heappush(heap1, (p, i))

ans = 0
for i in range(N):
  iR1 = R1[i]
  iR2 = R2[i]
  iL1 = L1[i]
  iL2 = L2[i]

  pR = abs(iR2 - iR1) * abs(iL1 - i)
  pL = abs(iL2 - iL1) * abs(iR1 - i)

  ans += (pR + pL) * P[i]

print(ans)
