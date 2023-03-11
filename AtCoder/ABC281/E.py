from collections import defaultdict
from heapq import heappop, heappush


class Heap:
  def __init__(self, reverse=False):
    self.heap = []
    self.sign = -1 if reverse else +1
    self.sum = 0
    self.deleted = defaultdict(int)
    self.len = 0

  def push(self, v):
    self.sum += v
    self.len += 1
    heappush(self.heap, self.sign * v)

  def pop(self):
    while True:
      v = heappop(self.heap) * self.sign
      if self.deleted[v] > 0:
        self.deleted[v] -= 1
      else:
        break

    self.sum -= v
    self.len -= 1
    return v

  def delete(self, v):
    self.deleted[v] += 1
    self.sum -= v
    self.len -= 1

  def peek(self):
    while True:
      peek = self.heap[0] * self.sign
      if self.deleted[peek] > 0:
        self.deleted[peek] -= 1
        heappop(self.heap)
      else:
        break

    return self.heap[0] * self.sign

  def __len__(self):
    return self.len


N, M, K = map(int, input().split())
A = list(map(int, input().split()))

heap1 = Heap(reverse=True)
heap2 = Heap()

for a in A[:M]:
  heap1.push(a)
  if len(heap1) > K: heap2.push(heap1.pop())

ans = [heap1.sum]

for d, a in zip(A, A[M:]):
  if d <= heap1.peek():
    heap1.delete(d)
    if len(heap2) > 0: heap1.push(heap2.pop())

  else:
    heap2.delete(d)

  heap1.push(a)
  if len(heap1) > K: heap2.push(heap1.pop())

  ans.append(heap1.sum)

print(*ans)
