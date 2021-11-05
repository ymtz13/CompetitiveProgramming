N, K = map(int, input().split())
A = list(map(int, input().split()))


def gcd(x, y):
  while x:
    x, y = y % x, x
  return y


g = A[0]
for a in A[1:]:
  g = gcd(g, a)

print('POSSIBLE' if K <= max(A) and K % g == 0 else 'IMPOSSIBLE')
