def gcd(x, y):
  while y: x, y = y, x%y
  return x

A, B = map(int, input().split())
LCM = A*B//gcd(A, B)
print(LCM if LCM<=10**18 else 'Large')
