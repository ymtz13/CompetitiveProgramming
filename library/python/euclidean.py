# gcd(a, b)とax+by=gcd(a,b)を満たすx,yを返す
def euclidean(a, b):
  x = w = 1
  y = z = 0
  while b:
    q = a // b
    r = a % b

    x, y, z, w = z, w, x - q * z, y - q * w
    a, b = b, r

  return a, x, y
