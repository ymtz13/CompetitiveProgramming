from heapq import heappop, heappush

N, K = map(int, input().split())
P = list(map(int, input().split()))

heap = []
for p in P[:K]:
  heappush(heap, p)

for p in P[K:]:
  print(heap[0])
  heappush(heap, p)
  heappop(heap)

print(heap[0])
