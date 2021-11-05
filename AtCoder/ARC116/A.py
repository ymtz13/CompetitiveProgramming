T = int(input())
for _ in range(T):
  X = int(input())
  n = 0
  while X%2==0:
    X//=2
    n += 1
  print('Odd' if n==0 else 'Same' if n==1 else 'Even')
