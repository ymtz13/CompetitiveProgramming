from heapq import heappop, heappush

T = int(input())

def solve(R):
  i = 0
  heap = []
  p = 1
  while i < len(R):
    l, r = R[i]
    p = max(p, l)

    while i < len(R) and R[i][0] == p:
      heappush(heap, R[i][1])
      i += 1

    while heap:
      while i < len(R) and R[i][0] == p:
        heappush(heap, R[i][1])
        i += 1

      r = heappop(heap)
      if r < p: return 'No'
      p += 1

  return 'Yes'


for _ in range(T):
  N = int(input())
  R = sorted([tuple(map(int, input().split())) for _ in range(N)])
  print(solve(R))
