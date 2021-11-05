from heapq import heappush, heappop

N = int(input())
A = list(map(int, input().split()))

P = [None] * N

for i, a in enumerate(A):
  P[a - 1] = i

R = [None] * N
L = [None] * N

heap = []
for i, a in enumerate(A + [0]):
  while heap and heap[0] < -a:
    v = -heappop(heap)
    R[v - 1] = i

  heappush(heap, -a)

heap = []
for i, a in enumerate(A[::-1] + [0]):
  i = N - 1 - i
  while heap and heap[0] < -a:
    v = -heappop(heap)
    L[v - 1] = i

  heappush(heap, -a)

ans = 0
for a, (p, r, l) in enumerate(zip(P, R, L)):
  ans += (a + 1) * (p - l) * (r - p)

print(ans)
