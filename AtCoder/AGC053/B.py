from heapq import heappop, heappush

N = int(input())
V = list(map(int, input().split()))

ans = sum(V)
heap = []

for v1, v2 in zip(V[N-1::-1], V[N:]):
  heappush(heap, v1)
  heappush(heap, v2)
  ans -= heappop(heap)

print(ans)
