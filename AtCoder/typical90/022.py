def gcd(x, y):
  while y: x, y = y, x%y
  return x

A, B, C = map(int, input().split())
g = gcd(gcd(A, B), C)
print(A//g+B//g+C//g-3)
