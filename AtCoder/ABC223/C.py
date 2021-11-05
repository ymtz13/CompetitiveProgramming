N = int(input())
XL = [tuple(map(int, input().split())) for _ in range(N)]
XR = XL[::-1]
S = sum([a for a, _ in XL])

l = 0
r = S


def getTime(X, p):
  q = t = 0
  for a, b in X:
    if q + a < p:
      t += a / b
      q += a
    else:
      t += (p - q) / b
      break

  return t


while r - l > 1e-8:
  p = (r + l) / 2
  tL = getTime(XL, p)
  tR = getTime(XR, S - p)
  if tL < tR:
    l = p
  else:
    r = p

print(l)
