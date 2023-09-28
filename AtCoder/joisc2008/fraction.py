from heapq import heappop, heappush
from math import gcd

L = 50000


class F:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def cmp(self, rhs):
    return self.a * rhs.b - rhs.a * self.b

  def __lt__(self, rhs):
    return self.cmp(rhs) < 0

  def __eq__(self, rhs):
    return self.cmp(rhs) == 0

  def __le__(self, rhs):
    return self.cmp(rhs) <= 0

  def __str__(self):
    return str((self.a, self.b))


M, K = map(int, input().split())
heap = []
for m in range(2, M + 1):
  heappush(heap, F(1, m))

prev = F(0, 1)
ans = []
while heap:
  v = heappop(heap)

  if v != prev:
    ans.append(v)
    if len(ans) == K:
      a = v.a
      b = v.b
      g = gcd(a, b)
      print(a // g, b // g)
      exit()

  prev = v

  if v.a + 1 < v.b:
    heappush(heap, F(v.a + 1, v.b))

print(-1)