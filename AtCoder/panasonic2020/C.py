# va + vb < vc
# a + 2vab + b < c
# 2vab < c - a - b
# 4ab < (c - a - b)^2

a, b, c = map(int, input().split())
if a+b>c:
  print('No')
  exit()
lhs = 4*a*b
rhs = (c-a-b)**2
print('Yes' if lhs < rhs else 'No')
