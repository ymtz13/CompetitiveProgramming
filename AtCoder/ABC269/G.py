from collections import defaultdict, deque

INF = 1 << 20


class MinStack:
  def __init__(self):
    self.stack = deque()

  def append(self, x):
    self.stack.append((x, min(self.min(), x)))

  def pop(self):
    return self.stack.pop()[0]

  def min(self):
    if self.stack:
      return self.stack[-1][1]
    return INF

  def __length__(self):
    return len(self.stack)


class MinQueue:
  def __init__(self):
    self.stack1 = MinStack()
    self.stack2 = MinStack()

  def min(self):
    if len(self.stack1) or len(self.stack2):
      return min(self.stack1.min(), self.stack2.min())
    return INF


N, M = map(int, input().split())
S = 0
D = defaultdict(int)

for _ in range(N):
  A, B = map(int, input().split())
  S += A
  D[B - A] += 1

dp = [INF] * (M + 1)
dp[S] = 0

for diff, count in D.items():
  if diff == 0: continue

  if diff > 0:
    C = [0] * (M + 1)
    for i, (v, c) in enumerate(dp[:M + 1 - diff], C[:M + 1 - diff], diff):
      pass

for v in dp:
  print(-1 if v == INF else v)
