from heapq import heappop, heappush
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
M = 10**6


def solve(A):
  A1 = A[:N]
  A2 = A[N:]

  D = defaultdict(list)
  heap = []
  for i, a in enumerate(A1):
    heappush(heap, a * M + i)
    D[a].append(i)

  m = min(A1)

  ans = []
  x = None

  for i, (a1, a2) in enumerate(zip(A1, A2)):
    if a1 == m:
      if a2 <= a1:
        return [(a1, a2)]
      else:
        ans.append((a1, a2))
        x = i

  b = ans[0][1]
  b2 = -1
  for _, k in ans:
    if k != b:
      b2 = k
      break

  x += 1
  while x < N:
    #m = min(A1[x:])
    while heap:
      v = heappop(heap)
      m, i = v // M, v % M
      if i < x:
        m = None
      else:
        break
    if m is None: return ans

    if m > b:
      return ans

    if m == b:
      if b2 < b:
        return ans

    #for i, (a1, a2) in enumerate(zip(A1[x:], A2[x:]), x):
    #  if a1 == m:
    #    ans.append((a1, a2))
    #    x = i
    for i in D[m]:
      if i >= x:
        ans.append((m, A2[i]))
        x = max(x, i)
    x += 1

  return ans


ans = solve(A)
ans = [a[0] for a in ans] + [a[1] for a in ans]
print(' '.join(map(str, ans)))
