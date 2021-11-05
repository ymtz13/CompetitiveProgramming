from heapq import heappush, heappop

N = int(input())
H = list(map(int, input().split()))

S = [0]
heap = [10**10]
for h in H:
  x = 0
  while heap[0] < h:
    x += 1
    heappop(heap)

  S.append(S[-1] + x)
  heappush(heap, h)

for n, s in enumerate(S[:-1]):
  print(n - s)
