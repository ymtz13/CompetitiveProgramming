R, B = map(int, input().split())
x, y = map(int, input().split())


def solve(R, B, x, y):
  if R >= x * B: return B
  if B >= y * R: return R

  X = (R * y - B) / (x * y - 1)
  Y = (B * x - R) / (x * y - 1)

  #print(X * x + Y, R)
  #print(X + Y * y, B)

  ans = 0
  for p in range(int(X) - 1000, int(X) + 1000):
    r = R - p * x
    b = B - p

    q = min(r, b // y)
    if p >= 0 and q >= 0: ans = max(ans, p + q)

  for q in range(int(Y) - 1000, int(Y) + 1000):
    r = R - q
    b = B - q * y

    p = min(b, r // x)
    if p >= 0 and q >= 0: ans = max(ans, p + q)

  return ans

print(solve(R, B, x, y))
exit()


def solve2(R, B, x, y):
  ans = 0
  for nr in range(0, B + 1):
    nb = min(R - nr * x, (B - nr) // y)
    if nr >= 0 and nb >= 0: ans = max(ans, nr + nb)
  return ans


for R in range(1, 1000):
  for B in range(1, 10):
    s1 = solve(R, B, x, y)
    s2 = solve2(R, B, x, y)
    if s1 != s2:
      print(s1, s2, R, B)
