A, B = map(int, input().split())
if A == B:
  print('1.000')
  exit()

if B == 0:
  print('0.000')
  exit()

Q = B * 10000 // A
X = Q // 10 + (1 if Q % 10 >= 5 else 0)

print('0.{}'.format(X))
