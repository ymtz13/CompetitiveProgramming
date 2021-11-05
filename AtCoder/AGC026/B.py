T = int(input())


def gcd(x, y):
  while x:
    x, y = y % x, x
  return y


def solve(A, B, C, D):
  if D < B: return False
  if A < B: return False
  if C >= B - 1: return True
  if A % B > C: return False

  P = gcd(B, D)

  if A % P + B - P > C: return False
  return True


for _ in range(T):
  A, B, C, D = map(int, input().split())

  print('Yes' if solve(A, B, C, D) else 'No')
