from heapq import heappop, heappush

N, L = map(int, input().split())
A = list(map(int, input().split()))

S = sum(A)
if L - S > 0: A.append(L - S)

heap = sorted(A)

ans = 0
while len(heap) > 1:
  a = heappop(heap)
  b = heappop(heap)
  s = a + b
  heappush(heap, s)
  ans += s

print(ans)
