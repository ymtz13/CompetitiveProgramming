for _ in range(3):
  h0, m0, s0, h1, m1, s1 = map(int, input().split())
  t = (h1 - h0) * 3600 + (m1 - m0) * 60 + s1 - s0

  h = t // 3600
  m = (t % 3600) // 60
  s = t % 60
  print(h, m, s)
