N = int(input())


def f(p):
  for i in range(12, -1, -1):
    mask = (1 << i) - 1
    if p & mask < N: return p & mask


for p in range(N):
  p1 = p * 2
  p2 = p1 + 1

  print(f(p1) + 1, f(p2) + 1)
