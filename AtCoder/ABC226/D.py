def gcd(x, y):
  while x:
    x, y = y % x, x
  return y


N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
V = set()
for x1, y1 in P:
  for x2, y2 in P:
    a = x2 - x1
    b = y2 - y1
    if a < 0 or (a == 0 and b <= 0): continue

    if a == 0:
      V.add((0, 1))

    elif b == 0:
      V.add((1, 0))

    else:
      g = gcd(a, b)
      V.add((a // g, b // g))

#print(V)
print(len(V) * 2)
