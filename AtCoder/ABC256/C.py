from itertools import product

h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
for x11, x12, x21, x22 in product(range(1, 30), repeat=4):
  x13 = h1 - (x11 + x12)
  x23 = h2 - (x21 + x22)
  x31 = w1 - (x11 + x21)
  x32 = w2 - (x12 + x22)

  x33h = h3 - (x31 + x32)
  x33w = w3 - (x13 + x23)

  if x13 > 0 and x23 > 0 and x31 > 0 and x32 > 0 and x33h > 0 and x33h == x33w:
    ans += 1

print(ans)
