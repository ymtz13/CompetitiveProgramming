H, M = map(int, input().split())
for X in range(H * 60 + M, 10000):
  X %= 24 * 60

  h = X // 60
  m = X % 60

  h1 = h // 10
  h2 = h % 10
  m1 = m // 10
  m2 = m % 10

  hd = h1 * 10 + m1
  md = h2 * 10 + m2

  if 0 <= hd < 24 and 0 <= md < 60:
    print(h, m)
    exit()
