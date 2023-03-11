N, X, Y = map(int, input().split())


def dfsR(level):
  if level == 1: return 0
  return dfsR(level - 1) + dfsB(level) * X


def dfsB(level):
  if level == 1: return 1
  return dfsR(level - 1) + dfsB(level - 1) * Y

print(dfsR(N))
